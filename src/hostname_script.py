#!/usr/bin/env python3
"""
Script to print the hostname of the machine it's running on.
"""

import socket


def get_hostname():
    """
    Get the hostname of the current machine.
    
    Returns:
        str: The hostname of the machine
    """
    return socket.gethostname()


def main():
    """Main function to print the hostname."""
    hostname = get_hostname()
    print(f"Computer name: {hostname}")


if __name__ == "__main__":
    main()
