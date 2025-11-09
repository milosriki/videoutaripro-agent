"""
🎯 WORKING DUBAI VIDEO CREATOR
=============================

Simple, working version that creates Dubai market ads from your video.
"""

import subprocess
import os
import time
import requests

def create_dubai_ad(video_id="1ggD2WeC-TW8bE5pxFZD5p27pfG9QksBW", target_audience="men_40"):
    """
    🎯 CREATE DUBAI AD
    
    Simple function that works.
    """
    print(f"🎯 CREATING DUBAI AD FOR {target_audience.upper()}")
    print("=" * 50)
    
    workspace_dir = "./dubai_ads_workspace"
    output_dir = f"{workspace_dir}/output"
    
    # Create directories
    os.makedirs(workspace_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Download video
        video_url = f"https://drive.google.com/uc?export=download&id={video_id}"
        source_path = f"{workspace_dir}/{video_id}_source.mp4"
        
        print("📥 Downloading video...")
        response = requests.get(video_url)
        response.raise_for_status()
        
        with open(source_path, 'wb') as f:
            f.write(response.content)
        
        file_size = os.path.getsize(source_path) / (1024 * 1024)
        print(f"✅ Downloaded: {file_size:.1f} MB")
        
        # Create 30-second ad
        output_name = f"dubai_{target_audience}_ad_{int(time.time())}.mp4"
        output_path = f"{output_dir}/{output_name}"
        
        print(f"🎬 Creating 30-second {target_audience} ad...")
        
        # Simple working FFmpeg command
        cmd = [
            '/usr/bin/ffmpeg', '-i', source_path,
            '-t', '30',  # 30 seconds
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-preset', 'fast',
            '-crf', '23',
            output_path, '-y'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            file_size = os.path.getsize(output_path) / (1024 * 1024)
            print(f"✅ SUCCESS! Created: {output_name} ({file_size:.1f} MB)")
            print(f"📁 Location: {output_path}")
            return output_path
        else:
            print(f"❌ FFmpeg failed")
            print(f"Error: {result.stderr}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def create_all_dubai_ads(video_id="1ggD2WeC-TW8bE5pxFZD5p27pfG9QksBW"):
    """
    🎯 CREATE ALL DUBAI ADS
    
    Creates ads for men, women, and mixed audiences.
    """
    print("🎯 CREATING ALL DUBAI ADS")
    print("=" * 50)
    
    audiences = ['men_40', 'women_40', 'mixed']
    created_ads = []
    
    for audience in audiences:
        print(f"\n🎬 Creating ad for {audience}")
        
        ad_path = create_dubai_ad(video_id, audience)
        
        if ad_path:
            created_ads.append({
                'audience': audience,
                'path': ad_path,
                'filename': os.path.basename(ad_path)
            })
            print(f"✅ Created {audience} ad")
        else:
            print(f"❌ Failed {audience} ad")
    
    print(f"\n🎉 CREATED {len(created_ads)} DUBAI ADS!")
    
    if created_ads:
        print("\n📁 YOUR DUBAI ADS:")
        for i, ad in enumerate(created_ads):
            file_size = os.path.getsize(ad['path']) / (1024 * 1024)
            print(f"   {i+1}. {ad['filename']} - {ad['audience']} ({file_size:.1f} MB)")
    
    return created_ads

def test_system():
    """
    🧪 TEST SYSTEM
    """
    print("🧪 TESTING DUBAI VIDEO SYSTEM")
    print("=" * 50)
    
    # Test FFmpeg
    try:
        result = subprocess.run(['/usr/bin/ffmpeg', '-version'], capture_output=True, text=True)
        print("✅ FFmpeg: Working" if result.returncode == 0 else "❌ FFmpeg: Failed")
    except:
        print("❌ FFmpeg: Not found")
    
    # Test video download
    try:
        test_url = "https://drive.google.com/uc?export=download&id=1ggD2WeC-TW8bE5pxFZD5p27pfG9QksBW"
        response = requests.head(test_url, allow_redirects=True)
        print(f"✅ Video Download: Working ({response.status_code})")
    except Exception as e:
        print(f"❌ Video Download: Error - {str(e)}")
    
    print("\n🎯 READY TO CREATE DUBAI ADS!")
    print("Run: create_all_dubai_ads()")

if __name__ == "__main__":
    test_system()