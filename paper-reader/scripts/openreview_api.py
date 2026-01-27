#!/usr/bin/env python3
"""
OpenReview API Integration for Paper Reader Skill

This module provides functions to fetch paper reviews and discussions from OpenReview.
It supports both API v2 (current) and API v1 (legacy) for older conferences.

Usage:
    from scripts.openreview_api import OpenReviewFetcher, format_reviews_markdown

    fetcher = OpenReviewFetcher()

    # Method 1: Direct forum ID (fastest, if you have the URL)
    reviews = fetcher.get_reviews(forum_id="LzPWWPAdY4")

    # Method 2: Search by paper title
    result = fetcher.get_reviews_by_title("Attention Is All You Need")

    # Format for display
    print(format_reviews_markdown(result))

Note:
    For best results, use Google search: site:openreview.net [paper title]
    Then extract forum ID from URL and use get_reviews() directly.

Requirements:
    pip install openreview-py
"""

import re
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict

try:
    import openreview
    OPENREVIEW_AVAILABLE = True
except ImportError:
    OPENREVIEW_AVAILABLE = False

try:
    import requests  # noqa: F401
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


@dataclass
class PaperInfo:
    """Basic paper information from OpenReview."""
    forum_id: str
    title: str
    authors: List[str]
    abstract: str
    venue: str
    url: str
    decision: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ReviewInfo:
    """Review information from OpenReview."""
    review_id: str
    forum_id: str
    reviewer: str  # Anonymous ID like "Reviewer_1"
    rating: Optional[str] = None
    confidence: Optional[str] = None
    summary: Optional[str] = None
    strengths: Optional[str] = None
    weaknesses: Optional[str] = None
    questions: Optional[str] = None
    limitations: Optional[str] = None
    soundness: Optional[str] = None
    presentation: Optional[str] = None
    contribution: Optional[str] = None
    recommendation: Optional[str] = None
    raw_content: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DiscussionInfo:
    """Discussion/comment information from OpenReview."""
    comment_id: str
    forum_id: str
    author: str
    content: str
    reply_to: Optional[str] = None
    timestamp: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class OpenReviewFetcher:
    """
    Fetcher for OpenReview paper reviews and discussions.

    Supports:
    - Searching papers by title
    - Fetching reviews for a specific paper
    - Fetching discussion threads
    - Validating paper-review correspondence
    """

    # Common venue IDs for major ML conferences
    KNOWN_VENUES = {
        "neurips": "NeurIPS.cc",
        "nips": "NeurIPS.cc",
        "iclr": "ICLR.cc",
        "icml": "ICML.cc",
        "aaai": "AAAI.org",
        "cvpr": "CVPR",
        "eccv": "ECCV",
        "acl": "aclweb.org",
        "emnlp": "EMNLP",
        "naacl": "NAACL",
        "coling": "COLING",
    }

    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        """
        Initialize the OpenReview fetcher.

        Args:
            username: OpenReview username (optional, for authenticated access)
            password: OpenReview password (optional)
        """
        if not OPENREVIEW_AVAILABLE:
            raise ImportError(
                "openreview-py is not installed. "
                "Install it with: pip install openreview-py"
            )

        # Initialize API v2 client (current)
        self.client_v2 = openreview.api.OpenReviewClient(
            baseurl='https://api2.openreview.net',
            username=username,
            password=password
        )

        # Initialize API v1 client (legacy, for older conferences)
        self.client_v1 = openreview.Client(
            baseurl='https://api.openreview.net',
            username=username,
            password=password
        )

    def search_paper(
        self,
        title: str,
        venue: Optional[str] = None,
        year: Optional[int] = None,
        limit: int = 10
    ) -> List[PaperInfo]:
        """
        Search for papers by title.

        Args:
            title: Paper title to search for
            venue: Optional venue filter (e.g., "NeurIPS.cc/2023")
            year: Optional year filter
            limit: Maximum number of results

        Returns:
            List of PaperInfo objects matching the search
        """
        results = []

        # Try API v2 first
        try:
            notes = self._search_v2(title, venue, year, limit)
            for note in notes:
                paper = self._parse_paper_v2(note)
                if paper:
                    results.append(paper)
        except Exception as e:
            print(f"API v2 search failed: {e}")

        # If no results, try API v1
        if not results:
            try:
                notes = self._search_v1(title, venue, year, limit)
                for note in notes:
                    paper = self._parse_paper_v1(note)
                    if paper:
                        results.append(paper)
            except Exception as e:
                print(f"API v1 search failed: {e}")

        return results

    def _search_v2(
        self,
        title: str,
        venue: Optional[str],
        year: Optional[int],
        limit: int
    ) -> List:
        """Search using API v2."""
        results = []
        title_lower = title.lower()

        # OpenReview API v2 requires at least one of: invitation, forum, etc.
        # We need to search by venue/year to get results

        venues_to_try = []

        if venue:
            venues_to_try.append(venue)
        elif year:
            # Try common ML conference venues for the year
            venues_to_try = [
                f"ICLR.cc/{year}/Conference",
                f"NeurIPS.cc/{year}/Conference",
                f"ICML.cc/{year}/Conference",
            ]
        else:
            # Try recent years of major conferences
            import datetime
            current_year = datetime.datetime.now().year
            for y in range(current_year, current_year - 3, -1):
                venues_to_try.extend([
                    f"ICLR.cc/{y}/Conference",
                    f"NeurIPS.cc/{y}/Conference",
                    f"ICML.cc/{y}/Conference",
                ])

        for v in venues_to_try:
            try:
                invitation = f"{v}/-/Submission"
                # Get all notes and filter locally (API doesn't support partial title match)
                notes = list(self.client_v2.get_all_notes(invitation=invitation))

                # Filter by title locally
                for note in notes:
                    note_title = note.content.get('title', {}).get('value', '')
                    if title_lower in note_title.lower():
                        results.append(note)

                if results:
                    break  # Found results, stop searching
            except Exception:
                continue

        return results[:limit]

    def _search_v1(
        self,
        title: str,
        venue: Optional[str],
        year: Optional[int],
        limit: int
    ) -> List:
        """Search using API v1 (legacy)."""
        notes = list(openreview.tools.iterget_notes(
            self.client_v1,
            content={'title': title}
        ))
        return notes[:limit]

    def _parse_paper_v2(self, note) -> Optional[PaperInfo]:
        """Parse paper info from API v2 note."""
        try:
            content = note.content
            # Handle both API v2 formats (invitations vs invitation)
            invitations = getattr(note, 'invitations', []) or []
            invitation = getattr(note, 'invitation', None)
            venue_str = invitations[0] if invitations else (invitation or 'Unknown')
            venue = venue_str.split('/-/')[0] if '/-/' in venue_str else venue_str

            return PaperInfo(
                forum_id=note.forum,
                title=content.get('title', {}).get('value', 'Unknown'),
                authors=content.get('authors', {}).get('value', []),
                abstract=content.get('abstract', {}).get('value', ''),
                venue=venue,
                url=f"https://openreview.net/forum?id={note.forum}",
                decision=content.get('decision', {}).get('value')
            )
        except Exception:
            return None

    def _parse_paper_v1(self, note) -> Optional[PaperInfo]:
        """Parse paper info from API v1 note."""
        try:
            content = note.content
            return PaperInfo(
                forum_id=note.forum,
                title=content.get('title', 'Unknown'),
                authors=content.get('authors', []),
                abstract=content.get('abstract', ''),
                venue=note.invitation.split('/-/')[0] if note.invitation else 'Unknown',
                url=f"https://openreview.net/forum?id={note.forum}",
                decision=content.get('decision')
            )
        except Exception:
            return None

    def get_reviews(
        self,
        forum_id: str,
        include_meta_review: bool = True
    ) -> List[ReviewInfo]:
        """
        Get all reviews for a paper by its forum ID.

        Args:
            forum_id: The OpenReview forum ID of the paper
            include_meta_review: Whether to include meta-reviews/AC decisions

        Returns:
            List of ReviewInfo objects
        """
        reviews = []

        # Try API v2 first
        try:
            review_notes = self._get_reviews_v2(forum_id, include_meta_review)
            for note in review_notes:
                review = self._parse_review_v2(note)
                if review:
                    reviews.append(review)
        except Exception as e:
            print(f"API v2 review fetch failed: {e}")

        # If no results, try API v1
        if not reviews:
            try:
                review_notes = self._get_reviews_v1(forum_id, include_meta_review)
                for note in review_notes:
                    review = self._parse_review_v1(note)
                    if review:
                        reviews.append(review)
            except Exception as e:
                print(f"API v1 review fetch failed: {e}")

        return reviews

    def _get_reviews_v2(self, forum_id: str, include_meta_review: bool) -> List:
        """Get reviews using API v2."""
        # Get all notes in the forum
        notes = list(self.client_v2.get_all_notes(forum=forum_id))

        # Filter for reviews - API v2 uses 'invitations' (plural)
        review_notes = []
        for note in notes:
            # Check invitations (API v2 format)
            invitations = getattr(note, 'invitations', []) or []
            for inv in invitations:
                inv_lower = inv.lower()
                if 'official_review' in inv_lower:
                    review_notes.append(note)
                    break
                elif include_meta_review and ('meta_review' in inv_lower or 'decision' in inv_lower):
                    review_notes.append(note)
                    break

        return review_notes

    def _get_reviews_v1(self, forum_id: str, include_meta_review: bool) -> List:
        """Get reviews using API v1."""
        notes = list(openreview.tools.iterget_notes(
            self.client_v1,
            forum=forum_id
        ))

        review_notes = []
        for note in notes:
            if note.invitation:
                inv_lower = note.invitation.lower()
                if 'official_review' in inv_lower or 'review' in inv_lower:
                    review_notes.append(note)
                elif include_meta_review and ('meta_review' in inv_lower or 'decision' in inv_lower):
                    review_notes.append(note)

        return review_notes

    def _parse_review_v2(self, note) -> Optional[ReviewInfo]:
        """Parse review info from API v2 note."""
        try:
            content = note.content

            # Extract reviewer ID from signatures
            reviewer = "Unknown"
            if note.signatures:
                sig = note.signatures[0]
                if 'Reviewer' in sig:
                    reviewer = sig.split('/')[-1]
                elif 'Area_Chair' in sig or 'AC' in sig:
                    reviewer = "Area Chair"
                else:
                    reviewer = sig.split('/')[-1]

            # Helper to get value from content
            def get_val(key):
                if key in content:
                    val = content[key]
                    if isinstance(val, dict):
                        return val.get('value', '')
                    return val
                return None

            return ReviewInfo(
                review_id=note.id,
                forum_id=note.forum,
                reviewer=reviewer,
                rating=get_val('rating') or get_val('recommendation'),
                confidence=get_val('confidence'),
                summary=get_val('summary') or get_val('summary_of_the_paper'),
                strengths=get_val('strengths') or get_val('strengths_and_contributions'),
                weaknesses=get_val('weaknesses') or get_val('weaknesses_and_limitations'),
                questions=get_val('questions') or get_val('questions_for_authors'),
                limitations=get_val('limitations'),
                soundness=get_val('soundness'),
                presentation=get_val('presentation'),
                contribution=get_val('contribution'),
                recommendation=get_val('recommendation') or get_val('decision'),
                raw_content=dict(content) if content else None
            )
        except Exception:
            return None

    def _parse_review_v1(self, note) -> Optional[ReviewInfo]:
        """Parse review info from API v1 note."""
        try:
            content = note.content

            reviewer = "Unknown"
            if note.signatures:
                sig = note.signatures[0]
                if 'AnonReviewer' in sig:
                    reviewer = sig.split('/')[-1]
                elif 'Area_Chair' in sig:
                    reviewer = "Area Chair"
                else:
                    reviewer = sig.split('/')[-1]

            return ReviewInfo(
                review_id=note.id,
                forum_id=note.forum,
                reviewer=reviewer,
                rating=content.get('rating') or content.get('recommendation'),
                confidence=content.get('confidence'),
                summary=content.get('review') or content.get('summary'),
                strengths=content.get('strengths'),
                weaknesses=content.get('weaknesses'),
                questions=content.get('questions'),
                limitations=content.get('limitations'),
                soundness=content.get('soundness'),
                presentation=content.get('presentation'),
                contribution=content.get('contribution'),
                recommendation=content.get('recommendation') or content.get('decision'),
                raw_content=content
            )
        except Exception:
            return None

    def get_discussions(self, forum_id: str) -> List[DiscussionInfo]:
        """
        Get all discussion comments for a paper.

        Args:
            forum_id: The OpenReview forum ID

        Returns:
            List of DiscussionInfo objects
        """
        discussions = []

        try:
            notes = list(self.client_v2.get_all_notes(forum=forum_id))

            for note in notes:
                if note.invitation:
                    inv_lower = note.invitation.lower()
                    # Filter for comments/discussions (not reviews)
                    if 'comment' in inv_lower or 'discussion' in inv_lower or 'rebuttal' in inv_lower:
                        discussions.append(DiscussionInfo(
                            comment_id=note.id,
                            forum_id=note.forum,
                            author=note.signatures[0].split('/')[-1] if note.signatures else "Unknown",
                            content=str(note.content),
                            reply_to=note.replyto if hasattr(note, 'replyto') else None,
                            timestamp=str(note.cdate) if hasattr(note, 'cdate') else None
                        ))
        except Exception as e:
            print(f"Discussion fetch failed: {e}")

        return discussions

    def get_reviews_by_title(
        self,
        title: str,
        venue: Optional[str] = None,
        year: Optional[int] = None,
        verify: bool = True
    ) -> Dict[str, Any]:
        """
        Search for a paper by title and get its reviews.

        This is a convenience method that combines search and review fetching.

        Args:
            title: Paper title to search for
            venue: Optional venue filter
            year: Optional year filter
            verify: Whether to verify the paper matches the title

        Returns:
            Dictionary containing paper info and reviews
        """
        # Search for the paper
        papers = self.search_paper(title, venue, year, limit=5)

        if not papers:
            return {
                "success": False,
                "error": "No papers found matching the title",
                "paper": None,
                "reviews": []
            }

        # Find best match
        best_match = None
        best_score = 0.0

        for paper in papers:
            score = self._title_similarity(title, paper.title)
            if score > best_score:
                best_score = score
                best_match = paper

        # If no match found at all, use first result
        if best_match is None and papers:
            best_match = papers[0]
            best_score = self._title_similarity(title, best_match.title)

        if best_match is None:
            return {
                "success": False,
                "error": "No papers found matching the title",
                "paper": None,
                "reviews": []
            }

        if verify and best_score < 0.5:
            return {
                "success": False,
                "error": f"No paper found with sufficiently similar title. Best match: '{best_match.title}' (similarity: {best_score:.2f})",
                "paper": best_match.to_dict(),
                "reviews": []
            }

        # Get reviews
        reviews = self.get_reviews(best_match.forum_id)

        return {
            "success": True,
            "paper": best_match.to_dict(),
            "reviews": [r.to_dict() for r in reviews],
            "discussions": [],  # Can be fetched separately if needed
            "url": best_match.url
        }

    def _title_similarity(self, title1: str, title2: str) -> float:
        """Calculate simple title similarity score."""
        # Normalize titles
        t1 = set(title1.lower().split())
        t2 = set(title2.lower().split())

        # Remove common words
        stopwords = {'a', 'an', 'the', 'of', 'for', 'and', 'or', 'in', 'on', 'to', 'with'}
        t1 = t1 - stopwords
        t2 = t2 - stopwords

        if not t1 or not t2:
            return 0.0

        # Jaccard similarity
        intersection = len(t1 & t2)
        union = len(t1 | t2)

        return intersection / union if union > 0 else 0.0

    def validate_paper_review_match(
        self,
        paper_title: str,
        paper_authors: List[str],
        forum_id: str
    ) -> Dict[str, Any]:
        """
        Validate that a forum ID corresponds to the expected paper.

        This is important for ensuring we're fetching reviews for the correct paper.

        Args:
            paper_title: Expected paper title
            paper_authors: Expected author list
            forum_id: OpenReview forum ID to validate

        Returns:
            Validation result with match scores
        """
        try:
            # Get paper info from forum
            notes = list(self.client_v2.get_all_notes(forum=forum_id, limit=1))

            if not notes:
                return {
                    "valid": False,
                    "error": "Forum ID not found",
                    "title_match": 0.0,
                    "author_match": 0.0
                }

            paper = self._parse_paper_v2(notes[0])
            if not paper:
                return {
                    "valid": False,
                    "error": "Could not parse paper info",
                    "title_match": 0.0,
                    "author_match": 0.0
                }

            # Calculate title similarity
            title_score = self._title_similarity(paper_title, paper.title)

            # Calculate author overlap
            expected_authors = set(a.lower() for a in paper_authors)
            actual_authors = set(a.lower() for a in paper.authors)

            if expected_authors and actual_authors:
                author_score = len(expected_authors & actual_authors) / len(expected_authors | actual_authors)
            else:
                author_score = 0.0

            # Combined validation
            is_valid = title_score >= 0.5 or author_score >= 0.3

            return {
                "valid": is_valid,
                "title_match": title_score,
                "author_match": author_score,
                "found_title": paper.title,
                "found_authors": paper.authors,
                "url": paper.url
            }

        except Exception as e:
            return {
                "valid": False,
                "error": str(e),
                "title_match": 0.0,
                "author_match": 0.0
            }


def format_reviews_markdown(result: Dict[str, Any]) -> str:
    """
    Format review results as markdown for display.

    Args:
        result: Result from get_reviews_by_title()

    Returns:
        Formatted markdown string
    """
    if not result.get("success"):
        return f"## OpenReview Search Failed\n\n**Error**: {result.get('error', 'Unknown error')}\n"

    paper = result.get("paper", {})
    reviews = result.get("reviews", [])

    md = []
    md.append(f"## OpenReview: {paper.get('title', 'Unknown')}\n")
    md.append(f"**Venue**: {paper.get('venue', 'Unknown')}")
    md.append(f"**URL**: {paper.get('url', 'N/A')}")
    md.append(f"**Decision**: {paper.get('decision', 'N/A')}\n")

    if not reviews:
        md.append("*No reviews found for this paper.*\n")
        return "\n".join(md)

    md.append(f"### Reviews ({len(reviews)} total)\n")

    for i, review in enumerate(reviews, 1):
        md.append(f"#### {review.get('reviewer', f'Reviewer {i}')}")

        if review.get('rating'):
            md.append(f"**Rating**: {review['rating']}")
        if review.get('confidence'):
            md.append(f"**Confidence**: {review['confidence']}")
        if review.get('soundness'):
            md.append(f"**Soundness**: {review['soundness']}")
        if review.get('presentation'):
            md.append(f"**Presentation**: {review['presentation']}")
        if review.get('contribution'):
            md.append(f"**Contribution**: {review['contribution']}")

        md.append("")

        if review.get('summary'):
            md.append(f"**Summary**:\n{review['summary']}\n")
        if review.get('strengths'):
            md.append(f"**Strengths**:\n{review['strengths']}\n")
        if review.get('weaknesses'):
            md.append(f"**Weaknesses**:\n{review['weaknesses']}\n")
        if review.get('questions'):
            md.append(f"**Questions**:\n{review['questions']}\n")
        if review.get('limitations'):
            md.append(f"**Limitations**:\n{review['limitations']}\n")

        md.append("---\n")

    return "\n".join(md)


def extract_forum_id(url_or_id: str) -> Optional[str]:
    """
    Extract forum ID from OpenReview URL or return the ID if already extracted.

    Args:
        url_or_id: Either a full OpenReview URL or just the forum ID

    Returns:
        The forum ID string, or None if extraction failed

    Examples:
        >>> extract_forum_id("https://openreview.net/forum?id=LzPWWPAdY4")
        'LzPWWPAdY4'
        >>> extract_forum_id("LzPWWPAdY4")
        'LzPWWPAdY4'
    """
    if not url_or_id:
        return None

    # If it's already just an ID (no URL structure)
    if 'openreview.net' not in url_or_id and '/' not in url_or_id:
        return url_or_id

    # Extract from URL
    import re
    match = re.search(r'[?&]id=([a-zA-Z0-9_-]+)', url_or_id)
    if match:
        return match.group(1)

    return None


# CLI interface for testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python openreview_api.py <paper_title> [venue] [year]")
        print("Example: python openreview_api.py 'Attention Is All You Need' NeurIPS.cc 2017")
        sys.exit(1)

    title = sys.argv[1]
    venue = sys.argv[2] if len(sys.argv) > 2 else None
    year = int(sys.argv[3]) if len(sys.argv) > 3 else None

    print(f"Searching for: {title}")
    if venue:
        print(f"Venue filter: {venue}")
    if year:
        print(f"Year filter: {year}")

    fetcher = OpenReviewFetcher()
    result = fetcher.get_reviews_by_title(title, venue, year)

    print("\n" + "="*60 + "\n")
    print(format_reviews_markdown(result))
