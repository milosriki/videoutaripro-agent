#!/usr/bin/env python3
"""
🎬 VideoUtariPro Agent Demo
==========================

Demonstration of AI video marketing automation capabilities.
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from ai_automation.YOUR_AI_VIDEO_SYSTEM import business_videos, wellness_videos, testimonial_videos

def run_complete_demo():
    """
    🎬 RUN COMPLETE DEMO
    
    Demonstrates all AI automation capabilities.
    """
    print("🎬 VIDEOUTARIPRO AGENT - COMPLETE DEMO")
    print("=" * 60)
    print("AI-Powered Video Marketing Automation for Dubai Market")
    
    demos = [
        {
            'name': 'Business Avatar Demo',
            'function': business_videos,
            'folder': 'Demo_Business_Videos',
            'description': 'HeyGen business avatars for Dubai men 40+ executives'
        },
        {
            'name': 'Wellness Avatar Demo', 
            'function': wellness_videos,
            'folder': 'Demo_Wellness_Videos',
            'description': 'HeyGen wellness avatars for Dubai women 40+ sophisticated'
        },
        {
            'name': 'Testimonial Demo',
            'function': testimonial_videos,
            'folder': 'Demo_Testimonial_Videos',
            'description': 'Client testimonials for all Dubai audiences'
        }
    ]
    
    results = []
    
    for demo in demos:
        print(f"\n🎯 RUNNING: {demo['name']}")
        print("=" * 50)
        print(f"📁 Folder: {demo['folder']}")
        print(f"📝 Description: {demo['description']}")
        
        try:
            result = demo['function'](demo['folder'])
            
            if result and result.get('success'):
                print(f"✅ {demo['name']}: SUCCESS!")
                print(f"   📋 Strategy: {result.get('strategy_file', 'Generated')}")
                print(f"   🎭 Avatar: {result.get('avatar_type', 'Unknown')}")
                results.append({'demo': demo['name'], 'success': True, 'result': result})
            else:
                print(f"❌ {demo['name']}: FAILED")
                results.append({'demo': demo['name'], 'success': False, 'result': None})
                
        except Exception as e:
            print(f"❌ {demo['name']}: ERROR - {str(e)}")
            results.append({'demo': demo['name'], 'success': False, 'result': None})
    
    # Summary
    print(f"\n📊 DEMO RESULTS SUMMARY")
    print("=" * 50)
    
    successful_demos = [r for r in results if r['success']]
    
    print(f"✅ Successful demos: {len(successful_demos)}/{len(results)}")
    
    for result in results:
        status = "✅ SUCCESS" if result['success'] else "❌ FAILED"
        print(f"   {result['demo']}: {status}")
    
    if len(successful_demos) == len(results):
        print(f"\n🎉 ALL DEMOS SUCCESSFUL!")
        print("🤖 VideoUtariPro Agent is fully operational!")
        print("🎯 Ready for production use with Dubai video marketing!")
    else:
        print(f"\n⚠️ Some demos failed - check configuration")
    
    return results

def quick_test():
    """
    🧪 QUICK TEST
    
    Quick test of core functionality.
    """
    print("🧪 VIDEOUTARIPRO AGENT - QUICK TEST")
    print("=" * 50)
    
    try:
        # Test business avatar automation
        print("🎯 Testing business avatar automation...")
        result = business_videos("Quick_Test_Folder")
        
        if result and result.get('success'):
            print("✅ Quick test: SUCCESS!")
            print(f"📋 Strategy generated: {result.get('strategy_file', 'Yes')}")
            return True
        else:
            print("❌ Quick test: FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Quick test error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🎬 VideoUtariPro Agent Demo")
    print("Choose demo type:")
    print("1. Complete Demo (all avatar types)")
    print("2. Quick Test (business avatar only)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        run_complete_demo()
    elif choice == "2":
        quick_test()
    else:
        print("Running complete demo by default...")
        run_complete_demo()