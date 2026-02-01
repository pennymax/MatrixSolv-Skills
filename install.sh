#!/bin/bash

# MatrixSolv-Skills Installer
# Automatically detects environment and installs skills to Claude Code and/or Codex

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory (where the skills are located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Available skills
SKILLS=("paper-reader" "deep-learning-training-recipe" "skill-from-masters" "binance-data")

# Potential installation directories
CLAUDE_CODE_DIR="$HOME/.claude/skills"
CODEX_DIR="$HOME/.codex/skills"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         MatrixSolv-Skills Installer                        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Function to print status
print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[i]${NC} $1"
}

# Function to detect environment
detect_environment() {
    local found_env=0

    echo -e "${BLUE}Detecting environment...${NC}"
    echo ""

    # Check for Claude Code
    if [ -d "$HOME/.claude" ]; then
        print_status "Claude Code detected ($HOME/.claude)"
        CLAUDE_CODE_FOUND=true
        found_env=1
    else
        print_warning "Claude Code not detected"
        CLAUDE_CODE_FOUND=false
    fi

    # Check for Codex
    if [ -d "$HOME/.codex" ]; then
        print_status "Codex detected ($HOME/.codex)"
        CODEX_FOUND=true
        found_env=1
    else
        print_warning "Codex not detected"
        CODEX_FOUND=false
    fi

    echo ""

    if [ $found_env -eq 0 ]; then
        print_error "No supported environment detected!"
        echo ""
        echo "Supported environments:"
        echo "  - Claude Code (~/.claude)"
        echo "  - Codex (~/.codex)"
        echo ""
        echo "Would you like to create the directories anyway? (y/n)"
        read -r response
        if [[ "$response" =~ ^[Yy]$ ]]; then
            echo ""
            echo "Select environment to set up:"
            echo "  1) Claude Code"
            echo "  2) Codex"
            echo "  3) Both"
            read -r choice
            case $choice in
                1)
                    mkdir -p "$CLAUDE_CODE_DIR"
                    CLAUDE_CODE_FOUND=true
                    print_status "Created Claude Code skills directory"
                    ;;
                2)
                    mkdir -p "$CODEX_DIR"
                    CODEX_FOUND=true
                    print_status "Created Codex skills directory"
                    ;;
                3)
                    mkdir -p "$CLAUDE_CODE_DIR"
                    mkdir -p "$CODEX_DIR"
                    CLAUDE_CODE_FOUND=true
                    CODEX_FOUND=true
                    print_status "Created both skills directories"
                    ;;
                *)
                    print_error "Invalid choice. Exiting."
                    exit 1
                    ;;
            esac
        else
            exit 1
        fi
    fi
}

# Function to install skills to a directory
install_skills() {
    local target_dir="$1"
    local env_name="$2"

    echo -e "${BLUE}Installing skills to $env_name...${NC}"

    # Create skills directory if it doesn't exist
    mkdir -p "$target_dir"

    for skill in "${SKILLS[@]}"; do
        local source_path="$SCRIPT_DIR/$skill"
        local target_path="$target_dir/$skill"

        if [ -d "$source_path" ]; then
            # Remove existing skill if present
            if [ -d "$target_path" ]; then
                print_warning "Updating existing skill: $skill"
                rm -rf "$target_path"
            fi

            # Copy skill
            cp -r "$source_path" "$target_path"
            print_status "Installed: $skill"
        else
            print_error "Skill not found: $skill"
        fi
    done

    echo ""
}

# Function to verify installation
verify_installation() {
    local target_dir="$1"
    local env_name="$2"
    local success=true

    echo -e "${BLUE}Verifying $env_name installation...${NC}"

    for skill in "${SKILLS[@]}"; do
        local skill_path="$target_dir/$skill"
        local skill_file="$skill_path/SKILL.md"

        if [ -f "$skill_file" ]; then
            print_status "$skill - OK"
        else
            print_error "$skill - SKILL.md not found"
            success=false
        fi
    done

    echo ""
    return 0
}

# Function to show installed skills info
show_skills_info() {
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                   Installed Skills                         ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""

    echo -e "${GREEN}paper-reader${NC}"
    echo "  Structured methodology for reading ML/Quant research papers"
    echo "  Usage: /paper-reader <url/path> [--mode quick|deep|implement|critical]"
    echo ""

    echo -e "${GREEN}deep-learning-training-recipe${NC}"
    echo "  Systematic methodology for training neural networks"
    echo "  Triggers: 'train model', 'debug neural network', 'model not converging'"
    echo ""

    echo -e "${GREEN}skill-from-masters${NC}"
    echo "  Create high-quality skills based on proven expert methodologies"
    echo "  Triggers: 'help me create a skill for X', 'I want to make a skill that does Y'"
    echo ""

    echo -e "${GREEN}binance-data${NC}"
    echo "  Binance public historical data query and download assistant"
    echo "  Triggers: 'Binance data', 'download klines', 'funding rate', 'crypto historical data'"
    echo ""
}

# Main installation flow
main() {
    # Check if running from correct directory
    if [ ! -f "$SCRIPT_DIR/README.md" ]; then
        print_error "Please run this script from the MatrixSolv-Skills directory"
        exit 1
    fi

    # Detect environment
    detect_environment

    # Apply command line filters
    if [ "$INSTALL_CLAUDE_ONLY" = true ]; then
        CODEX_FOUND=false
    fi
    if [ "$INSTALL_CODEX_ONLY" = true ]; then
        CLAUDE_CODE_FOUND=false
    fi

    echo ""

    # Install to Claude Code if detected
    if [ "$CLAUDE_CODE_FOUND" = true ]; then
        install_skills "$CLAUDE_CODE_DIR" "Claude Code"
        verify_installation "$CLAUDE_CODE_DIR" "Claude Code"
    fi

    # Install to Codex if detected
    if [ "$CODEX_FOUND" = true ]; then
        install_skills "$CODEX_DIR" "Codex"
        verify_installation "$CODEX_DIR" "Codex"
    fi

    # Show summary
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║              Installation Complete!                        ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""

    if [ "$CLAUDE_CODE_FOUND" = true ]; then
        print_status "Skills installed to: $CLAUDE_CODE_DIR"
    fi

    if [ "$CODEX_FOUND" = true ]; then
        print_status "Skills installed to: $CODEX_DIR"
    fi

    echo ""
    show_skills_info

    echo -e "${YELLOW}Note: Restart your Claude Code or Codex session to load the new skills.${NC}"
    echo ""
}

# Parse command line arguments
INSTALL_CLAUDE_ONLY=false
INSTALL_CODEX_ONLY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --claude-code-only)
            INSTALL_CLAUDE_ONLY=true
            shift
            ;;
        --codex-only)
            INSTALL_CODEX_ONLY=true
            shift
            ;;
        --help|-h)
            echo "MatrixSolv-Skills Installer"
            echo ""
            echo "Usage: ./install.sh [options]"
            echo ""
            echo "Options:"
            echo "  --claude-code-only  Install only to Claude Code"
            echo "  --codex-only        Install only to Codex"
            echo "  --help, -h          Show this help message"
            echo ""
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Run main function
main
