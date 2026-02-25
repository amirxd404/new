#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Facebook Dumper Launcher - Choose between Instagram connected or without Instagram
Author: SHAJON
GitHub: SHAJON-404
"""

import os
import sys
import platform
from pathlib import Path


# ================== COLORS ==================

class Colors:
    """Simple color scheme"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Bright variants
    BRIGHT_RED = '\033[91;1m'
    BRIGHT_GREEN = '\033[92;1m'
    BRIGHT_YELLOW = '\033[93;1m'
    BRIGHT_BLUE = '\033[94;1m'
    BRIGHT_MAGENTA = '\033[95;1m'
    BRIGHT_CYAN = '\033[96;1m'


class Config:
    """Simple configuration"""
    
    def __init__(self):
        self.c = Colors()
        
        # Color shortcuts
        self.r = self.c.RED
        self.g = self.c.GREEN
        self.y = self.c.YELLOW
        self.b = self.c.BLUE
        self.p = self.c.MAGENTA
        self.cc = self.c.CYAN
        self.w = self.c.WHITE
        self.br = self.c.BRIGHT_RED
        self.bg = self.c.BRIGHT_GREEN
        self.by = self.c.BRIGHT_YELLOW
        self.bb = self.c.BRIGHT_BLUE
        self.bp = self.c.BRIGHT_MAGENTA
        self.bc = self.c.BRIGHT_CYAN
        
        # Platform detection
        system = platform.system().lower()
        self.is_termux = os.path.exists("/data/data/com.termux") or "com.termux" in os.environ.get("PREFIX", "")
        
        if self.is_termux:
            self.clear_cmd = "clear"
        elif system == "windows":
            self.clear_cmd = "cls"
            try:
                import colorama
                colorama.init()
            except ImportError:
                os.system("")
        else:
            self.clear_cmd = "clear"
        
        self.script_dir = Path(__file__).parent.resolve()
    
    def clear_screen(self):
        """Clear screen"""
        os.system(self.clear_cmd)
        self.show_banner()
    
    def show_banner(self):
        """Display banner"""
        banner = f"""
{self.bc}╔══════════════════════════════════════════════════════════════╗
{self.bc}║  {self.bg}███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ {self.bc}║
{self.bc}║  {self.bg}██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔════╝ {self.bc}║
{self.bc}║  {self.bg}█████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║  ███╗{self.bc}║
{self.bc}║  {self.bg}██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║{self.bc}║
{self.bc}║  {self.bg}██║     ██║  ██║╚██████╗███████╗██║  ██║╚██████╔╝╚██████╔╝{self.bc}║
{self.bc}║  {self.bg}╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ {self.bc}║
{self.bc}╚══════════════════════════════════════════════════════════════╝{self.w}
        """
        print(banner)
        self.linex()
    
    def linex(self, char="━", length=56):
        """Print separator line"""
        print(f"{self.bc}{char * length}{self.w}")
    
    def status(self, text, status_type="info"):
        """Status messages"""
        icons = {
            "success": f"{self.bg}✓{self.w}",
            "error": f"{self.br}✗{self.w}",
            "warning": f"{self.by}⚠{self.w}",
            "info": f"{self.bc}ℹ{self.w}",
        }
        icon = icons.get(status_type, icons["info"])
        return f"  {icon}  {text}"


class Launcher:
    """Main launcher application"""
    
    def __init__(self):
        self.config = Config()
    
    def _get_input(self, prompt):
        """Get user input"""
        return input(f"{self.config.bc}└─➤{self.config.w} {prompt}: ").strip()
    
    def run(self):
        """Main launcher"""
        try:
            self.config.clear_screen()
            
            print(f"{self.config.bc}┌─ 🔐 SELECT DUMP METHOD ────────────────────────")
            print(f"{self.config.bc}│{self.config.w}  {self.config.by}[1]{self.config.w}  📱 Instagram Connected Method")
            print(f"{self.config.bc}│{self.config.w}      (myfilee.cpython-312.so)")
            print(f"{self.config.bc}│{self.config.w}  {self.config.bg}[2]{self.config.w}  🍪 Without Instagram Method")
            print(f"{self.config.bc}│{self.config.w}      (fileexd.cpython-312.so)")
            print(f"{self.config.bc}└────────────────────────────────────────────")
            self.config.linex()
            
            choice = self._get_input("Choose option (1 or 2)")
            
            if choice == '1':
                # Instagram connected method
                print(self.config.status("Loading Instagram connected method...", "info"))
                try:
                    import myfilee
                    print(self.config.status("✅ Instagram connected method loaded!", "success"))
                    self.config.linex()
                    myfilee.main()
                except ImportError as e:
                    print(self.config.status(f"❌ Failed to import myfilee: {e}", "error"))
                    print(self.config.status("Make sure myfilee.cpython-312.so exists", "warning"))
                    
            elif choice == '2':
                # Without Instagram method
                print(self.config.status("Loading without Instagram method...", "info"))
                try:
                    import fileexd
                    print(self.config.status("✅ Without Instagram method loaded!", "success"))
                    self.config.linex()
                    fileexd.menu()
                except ImportError as e:
                    print(self.config.status(f"❌ Failed to import fileexd: {e}", "error"))
                    print(self.config.status("Make sure fileexd.cpython-312.so exists", "warning"))
            else:
                print(self.config.status("❌ Invalid option", "error"))
                self.config.linex()
                input(f"{self.config.bc}└─{self.config.w} Press Enter to exit...")
                sys.exit(1)
                
        except KeyboardInterrupt:
            print(f"\n{self.config.status('👋 Goodbye!', 'info')}")
            sys.exit(0)
        except Exception as e:
            print(f"\n{self.config.status(f'❌ Error: {e}', 'error')}")
            sys.exit(1)


# ================== MAIN ==================

def main():
    """Entry point"""
    launcher = Launcher()
    launcher.run()


if __name__ == "__main__":
    main()