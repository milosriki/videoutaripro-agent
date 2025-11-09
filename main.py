#!/usr/bin/env python3
"""
🎬 VideoUtariPro Agent - Main Entry Point
========================================

AI-Powered Video Marketing Automation for Dubai Market

Usage:
    python main.py --avatar heygen_business --folder "My_Business_Videos"
    python main.py --avatar heygen_wellness --folder "My_Wellness_Videos"
    python main.py --avatar testimonial --folder "My_Testimonials"
"""

import sys
import os
import argparse
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from ai_automation.YOUR_AI_VIDEO_SYSTEM import business_videos, wellness_videos, testimonial_videos
from config.settings import *

def main():
    """
    🎯 MAIN ENTRY POINT
    
    Command-line interface for VideoUtariPro Agent.
    """
    parser = argparse.ArgumentParser(
        description="🎬 VideoUtariPro Agent - AI Video Marketing Automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --avatar heygen_business --folder "My_Business_Videos"
  python main.py --avatar heygen_wellness --folder "My_Wellness_Videos"  
  python main.py --avatar testimonial --folder "My_Testimonials"
  python main.py --demo  # Run demo with sample video
        """
    )
    
    parser.add_argument(
        '--avatar', 
        choices=['heygen_business', 'heygen_wellness', 'testimonial'],
        help='Avatar type for video processing'
    )
    
    parser.add_argument(
        '--folder',
        type=str,
        help='Folder path containing videos to process'
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run demo with sample video'
    )
    
    parser.add_argument(
        '--config',
        action='store_true',
        help='Show current configuration'
    )
    
    args = parser.parse_args()
    
    print("🎬 VideoUtariPro Agent - AI Video Marketing Automation")
    print("=" * 60)
    print("Ultimate AI-powered video marketing system for Dubai market")
    
    if args.config:
        show_configuration()
        return
    
    if args.demo:
        run_demo()
        return
    
    if not args.avatar or not args.folder:
        print("❌ Error: Both --avatar and --folder are required")
        parser.print_help()
        return
    
    # Run AI automation based on avatar type
    print(f"\n🎯 Processing {args.avatar} videos from: {args.folder}")
    
    try:
        if args.avatar == 'heygen_business':
            result = business_videos(args.folder)
        elif args.avatar == 'heygen_wellness':
            result = wellness_videos(args.folder)
        elif args.avatar == 'testimonial':
            result = testimonial_videos(args.folder)
        
        if result and result.get('success'):
            print(f"\n🎉 SUCCESS! AI automation complete!")
            print(f"📋 Strategy file: {result.get('strategy_file', 'Unknown')}")
            print(f"🎯 Avatar: {result.get('avatar_type', 'Unknown')}")
            print(f"📁 Folder: {result.get('folder_path', 'Unknown')}")
        else:
            print("❌ AI automation failed")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def show_configuration():
    """Show current configuration"""
    
    print("🔧 CURRENT CONFIGURATION")
    print("=" * 50)
    print(f"🤖 Google AI API Key: {GOOGLE_AI_API_KEY[:20]}...")
    print(f"🎭 Google AI Model: {GOOGLE_AI_MODEL}")
    print(f"🏗️ Google Cloud Project: {GOOGLE_CLOUD_PROJECT}")
    print(f"📧 Google Cloud Account: {GOOGLE_CLOUD_ACCOUNT}")
    print(f"🎬 Submagic API Key: {SUBMAGIC_API_KEY[:20]}...")
    print(f"🤖 Dubai Agent ID: {DUBAI_AGENT_ID}")
    
    print(f"\n🎯 AVATAR CONFIGURATIONS:")
    for avatar, config in AVATAR_CONFIGS.items():
        print(f"   {avatar}: {config['target_audience']} - {config['conversion_focus']}")
    
    print(f"\n📱 PLATFORM SPECIFICATIONS:")
    for platform, specs in PLATFORM_SPECS.items():
        print(f"   {platform}: {specs['width']}x{specs['height']} @ {specs['fps']}fps")

def run_demo():
    """Run demo with sample video"""
    
    print("🎬 RUNNING VIDEOUTARIPRO AGENT DEMO")
    print("=" * 50)
    print("Demonstrating AI automation with sample video")
    
    try:
        # Demo business avatar automation
        print("\n🎯 DEMO: Business Avatar Automation")
        business_result = business_videos("Demo_Business_Folder")
        
        if business_result and business_result.get('success'):
            print("✅ Business automation demo: SUCCESS!")
        
        # Demo wellness avatar automation
        print("\n🎯 DEMO: Wellness Avatar Automation")
        wellness_result = wellness_videos("Demo_Wellness_Folder")
        
        if wellness_result and wellness_result.get('success'):
            print("✅ Wellness automation demo: SUCCESS!")
        
        print(f"\n🎉 DEMO COMPLETE!")
        print("🤖 VideoUtariPro Agent is ready for production!")
        
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")

if __name__ == "__main__":
    main()