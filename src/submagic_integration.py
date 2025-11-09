"""
🎬 SUBMAGIC API INTEGRATION - COMPLETE VIDEO MARKETING AUTOMATION
================================================================

This integration provides complete access to Submagic's AI-powered video editing API
for creating viral video ads with automated captions, B-roll, and professional templates.

Key Features:
- AI Captions in 100+ languages
- Magic Clips (1 video → 20 viral clips)
- Professional templates (Hormozi, Clean, Bold)
- Automatic B-roll and zoom effects
- YouTube video processing
- Webhook notifications

Perfect for Dubai market targeting ladies over 40 with sophisticated, elegant messaging.
"""

import requests
import json
import time
import os
from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum

class SubmagicTemplate(Enum):
    """Professional templates optimized for different use cases"""
    # High-converting templates for Dubai market
    HORMOZI_1 = "Hormozi 1"  # Direct response style
    HORMOZI_2 = "Hormozi 2"  # Most popular for ads
    HORMOZI_3 = "Hormozi 3"  # Authority positioning
    HORMOZI_4 = "Hormozi 4"  # Luxury positioning
    HORMOZI_5 = "Hormozi 5"  # Elegant style
    
    # Clean, sophisticated styles
    CLEAN = "Clean"
    ELEGANT = "Elegant"
    MINIMAL = "Minimal"
    
    # Bold, attention-grabbing
    BOLD = "Bold"
    DYNAMIC = "Dynamic"
    
    # Personality-based (for personal branding)
    SARA = "Sara"
    DANIEL = "Daniel"
    MAYA = "Maya"
    DAVID = "David"

class ProjectStatus(Enum):
    """Project processing status"""
    PROCESSING = "processing"
    TRANSCRIBING = "transcribing"
    EXPORTING = "exporting"
    COMPLETED = "completed"
    FAILED = "failed"

class RemoveSilencePace(Enum):
    """Silence removal speed options"""
    NATURAL = "natural"
    FAST = "fast"
    EXTRA_FAST = "extra-fast"

@dataclass
class VideoMetadata:
    """Video file metadata"""
    width: int
    height: int
    duration: float
    fps: int

@dataclass
class SubmagicProject:
    """Submagic project data structure"""
    id: str
    title: str
    language: str
    status: ProjectStatus
    template_name: str
    webhook_url: Optional[str] = None
    transcription_status: Optional[str] = None
    magic_zooms: bool = True
    magic_brolls: bool = True
    magic_brolls_percentage: int = 75
    remove_silence_pace: RemoveSilencePace = RemoveSilencePace.FAST
    remove_bad_takes: bool = True
    video_metadata: Optional[VideoMetadata] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    download_url: Optional[str] = None

class SubmagicAPI:
    """
    🎯 SUBMAGIC API CLIENT - COMPLETE VIDEO MARKETING AUTOMATION
    
    This client provides full access to Submagic's AI-powered video editing capabilities,
    optimized for creating high-converting video ads for the Dubai market.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize Submagic API client
        
        Args:
            api_key: Your Submagic API key (format: sk-[64-char-hex])
        """
        if not api_key.startswith('sk-'):
            raise ValueError("API key must start with 'sk-'")
            
        self.api_key = api_key
        self.base_url = "https://api.submagic.co/v1"
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }
    
    def get_languages(self) -> List[Dict[str, str]]:
        """
        Get all supported languages for transcription
        
        Returns:
            List of language objects with 'name' and 'code' fields
        """
        response = requests.get(f"{self.base_url}/languages", headers=self.headers)
        response.raise_for_status()
        return response.json()["languages"]
    
    def get_templates(self) -> List[str]:
        """
        Get all available video templates
        
        Returns:
            List of template names
        """
        response = requests.get(f"{self.base_url}/templates", headers=self.headers)
        response.raise_for_status()
        return response.json()["templates"]
    
    def create_project_from_url(
        self,
        title: str,
        video_url: str,
        language: str = "en",
        template: Union[str, SubmagicTemplate] = SubmagicTemplate.HORMOZI_2,
        webhook_url: Optional[str] = None,
        dictionary: Optional[List[str]] = None,
        magic_zooms: bool = True,
        magic_brolls: bool = True,
        magic_brolls_percentage: int = 75,
        remove_silence_pace: RemoveSilencePace = RemoveSilencePace.FAST,
        remove_bad_takes: bool = True
    ) -> SubmagicProject:
        """
        🎬 CREATE PROJECT FROM VIDEO URL
        
        Perfect for processing existing videos or YouTube content into viral ads.
        
        Args:
            title: Project title
            video_url: URL to video file (Google Drive, YouTube, etc.)
            language: Language code (e.g., 'en', 'ar' for Arabic)
            template: Template name or SubmagicTemplate enum
            webhook_url: URL for completion notifications
            dictionary: Custom words for better transcription
            magic_zooms: Enable automatic zoom effects
            magic_brolls: Enable B-roll insertion
            magic_brolls_percentage: Percentage of B-roll to add (0-100)
            remove_silence_pace: Speed of silence removal
            remove_bad_takes: Remove filler words and bad takes
            
        Returns:
            SubmagicProject object with project details
        """
        template_name = template.value if isinstance(template, SubmagicTemplate) else template
        
        payload = {
            "title": title,
            "language": language,
            "videoUrl": video_url,
            "templateName": template_name,
            "magicZooms": magic_zooms,
            "magicBrolls": magic_brolls,
            "magicBrollsPercentage": magic_brolls_percentage,
            "removeSilencePace": remove_silence_pace.value,
            "removeBadTakes": remove_bad_takes
        }
        
        if webhook_url:
            payload["webhookUrl"] = webhook_url
        if dictionary:
            payload["dictionary"] = dictionary
            
        response = requests.post(f"{self.base_url}/projects", headers=self.headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        return self._parse_project_response(data)
    
    def upload_project(
        self,
        title: str,
        video_file_path: str,
        language: str = "en",
        template: Union[str, SubmagicTemplate] = SubmagicTemplate.HORMOZI_2,
        webhook_url: Optional[str] = None,
        dictionary: Optional[List[str]] = None,
        magic_zooms: bool = True,
        magic_brolls: bool = True,
        magic_brolls_percentage: int = 75,
        remove_silence_pace: RemoveSilencePace = RemoveSilencePace.FAST,
        remove_bad_takes: bool = True
    ) -> SubmagicProject:
        """
        📤 UPLOAD VIDEO FILE FOR PROCESSING
        
        Upload a local video file for AI processing and enhancement.
        
        Args:
            title: Project title
            video_file_path: Path to local video file
            language: Language code
            template: Template name or SubmagicTemplate enum
            webhook_url: URL for completion notifications
            dictionary: Custom words for better transcription
            magic_zooms: Enable automatic zoom effects
            magic_brolls: Enable B-roll insertion
            magic_brolls_percentage: Percentage of B-roll to add (0-100)
            remove_silence_pace: Speed of silence removal
            remove_bad_takes: Remove filler words and bad takes
            
        Returns:
            SubmagicProject object with project details
        """
        template_name = template.value if isinstance(template, SubmagicTemplate) else template
        
        # Prepare form data
        files = {'file': open(video_file_path, 'rb')}
        data = {
            'title': title,
            'language': language,
            'templateName': template_name,
            'magicZooms': str(magic_zooms).lower(),
            'magicBrolls': str(magic_brolls).lower(),
            'magicBrollsPercentage': str(magic_brolls_percentage),
            'removeSilencePace': remove_silence_pace.value,
            'removeBadTakes': str(remove_bad_takes).lower()
        }
        
        if webhook_url:
            data['webhookUrl'] = webhook_url
        if dictionary:
            data['dictionary'] = json.dumps(dictionary)
        
        # Use different headers for multipart upload
        upload_headers = {"x-api-key": self.api_key}
        
        try:
            response = requests.post(
                f"{self.base_url}/projects/upload", 
                headers=upload_headers, 
                files=files, 
                data=data
            )
            response.raise_for_status()
            
            result = response.json()
            return self._parse_project_response(result)
        finally:
            files['file'].close()
    
    def create_magic_clips(
        self,
        title: str,
        youtube_url: str,
        language: str = "en",
        webhook_url: Optional[str] = None,
        min_clip_length: int = 15,
        max_clip_length: int = 60
    ) -> Dict:
        """
        ✨ CREATE MAGIC CLIPS FROM YOUTUBE VIDEO
        
        Transform 1 YouTube video into 20+ viral short clips automatically.
        Perfect for scaling content creation for Dubai market.
        
        Args:
            title: Project title
            youtube_url: YouTube video URL
            language: Language code
            webhook_url: URL for completion notifications
            min_clip_length: Minimum clip duration in seconds
            max_clip_length: Maximum clip duration in seconds
            
        Returns:
            Magic clips project data
        """
        payload = {
            "title": title,
            "language": language,
            "youtubeUrl": youtube_url,
            "minClipLength": min_clip_length,
            "maxClipLength": max_clip_length
        }
        
        if webhook_url:
            payload["webhookUrl"] = webhook_url
            
        response = requests.post(f"{self.base_url}/magic-clips", headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def get_project(self, project_id: str) -> SubmagicProject:
        """
        📊 GET PROJECT STATUS AND DETAILS
        
        Check processing status and download completed videos.
        
        Args:
            project_id: Unique project identifier
            
        Returns:
            SubmagicProject with current status and download URL if completed
        """
        response = requests.get(f"{self.base_url}/projects/{project_id}", headers=self.headers)
        response.raise_for_status()
        
        data = response.json()
        return self._parse_project_response(data)
    
    def update_project(
        self,
        project_id: str,
        remove_silence_pace: Optional[RemoveSilencePace] = None,
        remove_bad_takes: Optional[bool] = None,
        items: Optional[List[Dict]] = None
    ) -> Dict:
        """
        🔄 UPDATE PROJECT SETTINGS
        
        Modify project settings or add custom media insertions.
        
        Args:
            project_id: Project to update
            remove_silence_pace: New silence removal pace
            remove_bad_takes: Enable/disable bad take removal
            items: Custom media items to insert
            
        Returns:
            Update confirmation
        """
        payload = {}
        
        if remove_silence_pace:
            payload["removeSilencePace"] = remove_silence_pace.value
        if remove_bad_takes is not None:
            payload["removeBadTakes"] = remove_bad_takes
        if items:
            payload["items"] = items
            
        response = requests.put(
            f"{self.base_url}/projects/{project_id}", 
            headers=self.headers, 
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def wait_for_completion(
        self, 
        project_id: str, 
        max_wait_time: int = 1800,  # 30 minutes
        check_interval: int = 30
    ) -> SubmagicProject:
        """
        ⏳ WAIT FOR PROJECT COMPLETION
        
        Poll project status until completion or timeout.
        
        Args:
            project_id: Project to monitor
            max_wait_time: Maximum wait time in seconds
            check_interval: Check interval in seconds
            
        Returns:
            Completed SubmagicProject with download URL
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            project = self.get_project(project_id)
            
            if project.status == ProjectStatus.COMPLETED:
                return project
            elif project.status == ProjectStatus.FAILED:
                raise Exception(f"Project {project_id} failed processing")
            
            print(f"⏳ Project {project_id} status: {project.status.value}")
            time.sleep(check_interval)
        
        raise TimeoutError(f"Project {project_id} did not complete within {max_wait_time} seconds")
    
    def download_video(self, project: SubmagicProject, output_path: str) -> str:
        """
        📥 DOWNLOAD COMPLETED VIDEO
        
        Download the processed video to local file.
        
        Args:
            project: Completed SubmagicProject
            output_path: Local path to save video
            
        Returns:
            Path to downloaded file
        """
        if not project.download_url:
            raise ValueError("Project does not have a download URL. Ensure it's completed.")
        
        response = requests.get(project.download_url)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        return output_path
    
    def _parse_project_response(self, data: Dict) -> SubmagicProject:
        """Parse API response into SubmagicProject object"""
        video_metadata = None
        if 'videoMetaData' in data:
            vm = data['videoMetaData']
            video_metadata = VideoMetadata(
                width=vm.get('width', 0),
                height=vm.get('height', 0),
                duration=vm.get('duration', 0.0),
                fps=vm.get('fps', 30)
            )
        
        return SubmagicProject(
            id=data['id'],
            title=data['title'],
            language=data['language'],
            status=ProjectStatus(data['status']),
            template_name=data.get('templateName', ''),
            webhook_url=data.get('webhookUrl'),
            transcription_status=data.get('transcriptionStatus'),
            magic_zooms=data.get('magicZooms', True),
            magic_brolls=data.get('magicBrolls', True),
            magic_brolls_percentage=data.get('magicBrollsPercentage', 75),
            remove_silence_pace=RemoveSilencePace(data.get('removeSilencePace', 'fast')),
            remove_bad_takes=data.get('removeBadTakes', True),
            video_metadata=video_metadata,
            created_at=data.get('createdAt'),
            updated_at=data.get('updatedAt'),
            download_url=data.get('downloadUrl')
        )

class SubmagicVideoMarketer:
    """
    🎯 SPECIALIZED VIDEO MARKETING CLASS FOR DUBAI MARKET
    
    Optimized workflows for creating high-converting video ads targeting
    Dubai ladies over 40 with sophisticated, elegant messaging.
    """
    
    def __init__(self, api_key: str):
        self.api = SubmagicAPI(api_key)
        
        # Dubai market optimization settings
        self.dubai_settings = {
            "language": "en",  # English for Dubai market
            "templates": {
                "luxury": SubmagicTemplate.HORMOZI_5,
                "authority": SubmagicTemplate.HORMOZI_3,
                "elegant": SubmagicTemplate.ELEGANT,
                "sophisticated": SubmagicTemplate.CLEAN
            },
            "magic_brolls_percentage": 60,  # Subtle for sophisticated audience
            "remove_silence_pace": RemoveSilencePace.NATURAL  # Natural pace for elegance
        }
    
    def create_luxury_ad(
        self,
        title: str,
        video_source: str,
        positioning: str = "luxury",
        webhook_url: Optional[str] = None
    ) -> SubmagicProject:
        """
        💎 CREATE LUXURY POSITIONING AD
        
        Create sophisticated video ad optimized for Dubai's affluent market.
        
        Args:
            title: Ad title
            video_source: Video URL or file path
            positioning: 'luxury', 'authority', 'elegant', or 'sophisticated'
            webhook_url: Completion notification URL
            
        Returns:
            SubmagicProject for the luxury ad
        """
        template = self.dubai_settings["templates"].get(positioning, SubmagicTemplate.HORMOZI_2)
        
        # Luxury market dictionary for better transcription
        luxury_dictionary = [
            "Dubai", "Emirates", "luxury", "premium", "exclusive", 
            "sophisticated", "elegant", "transformation", "wellness",
            "lifestyle", "investment", "quality", "results"
        ]
        
        if video_source.startswith('http'):
            return self.api.create_project_from_url(
                title=title,
                video_url=video_source,
                language=self.dubai_settings["language"],
                template=template,
                webhook_url=webhook_url,
                dictionary=luxury_dictionary,
                magic_zooms=True,
                magic_brolls=True,
                magic_brolls_percentage=self.dubai_settings["magic_brolls_percentage"],
                remove_silence_pace=self.dubai_settings["remove_silence_pace"],
                remove_bad_takes=True
            )
        else:
            return self.api.upload_project(
                title=title,
                video_file_path=video_source,
                language=self.dubai_settings["language"],
                template=template,
                webhook_url=webhook_url,
                dictionary=luxury_dictionary,
                magic_zooms=True,
                magic_brolls=True,
                magic_brolls_percentage=self.dubai_settings["magic_brolls_percentage"],
                remove_silence_pace=self.dubai_settings["remove_silence_pace"],
                remove_bad_takes=True
            )
    
    def create_viral_clips_from_youtube(
        self,
        youtube_url: str,
        title: str = "Viral Clips",
        webhook_url: Optional[str] = None
    ) -> Dict:
        """
        🔥 CREATE 20+ VIRAL CLIPS FROM 1 YOUTUBE VIDEO
        
        Perfect for scaling content creation - turn 1 long video into 20+ short clips.
        
        Args:
            youtube_url: YouTube video URL
            title: Project title
            webhook_url: Completion notification URL
            
        Returns:
            Magic clips project data
        """
        return self.api.create_magic_clips(
            title=title,
            youtube_url=youtube_url,
            language=self.dubai_settings["language"],
            webhook_url=webhook_url,
            min_clip_length=15,  # Perfect for Instagram Reels
            max_clip_length=60   # Perfect for TikTok
        )
    
    def process_and_download(
        self,
        title: str,
        video_source: str,
        output_path: str,
        positioning: str = "luxury",
        webhook_url: Optional[str] = None
    ) -> str:
        """
        🎬 COMPLETE WORKFLOW: PROCESS AND DOWNLOAD
        
        Full automation: upload/process video → wait for completion → download result.
        
        Args:
            title: Project title
            video_source: Video URL or file path
            output_path: Where to save the final video
            positioning: Marketing positioning style
            webhook_url: Completion notification URL
            
        Returns:
            Path to downloaded video file
        """
        print(f"🎬 Creating luxury ad: {title}")
        project = self.create_luxury_ad(title, video_source, positioning, webhook_url)
        
        print(f"⏳ Waiting for completion (Project ID: {project.id})")
        completed_project = self.api.wait_for_completion(project.id)
        
        print(f"📥 Downloading video to: {output_path}")
        return self.api.download_video(completed_project, output_path)

# 🎯 DUBAI MARKET OPTIMIZATION PRESETS
DUBAI_LUXURY_PRESETS = {
    "wellness_transformation": {
        "template": SubmagicTemplate.HORMOZI_5,
        "dictionary": ["wellness", "transformation", "Dubai", "lifestyle", "premium", "results"],
        "magic_brolls_percentage": 60,
        "positioning": "Elegant wellness transformation for sophisticated Dubai ladies"
    },
    
    "fitness_authority": {
        "template": SubmagicTemplate.HORMOZI_3,
        "dictionary": ["fitness", "health", "Dubai", "expert", "professional", "results"],
        "magic_brolls_percentage": 70,
        "positioning": "Authority-based fitness expertise"
    },
    
    "luxury_lifestyle": {
        "template": SubmagicTemplate.ELEGANT,
        "dictionary": ["luxury", "lifestyle", "Dubai", "exclusive", "premium", "sophisticated"],
        "magic_brolls_percentage": 50,
        "positioning": "Luxury lifestyle enhancement"
    },
    
    "business_success": {
        "template": SubmagicTemplate.HORMOZI_2,
        "dictionary": ["business", "success", "Dubai", "entrepreneur", "growth", "investment"],
        "magic_brolls_percentage": 75,
        "positioning": "Business success and growth"
    }
}

def create_submagic_client(api_key: Optional[str] = None) -> SubmagicVideoMarketer:
    """
    🚀 QUICK CLIENT CREATION
    
    Create a Submagic client optimized for Dubai video marketing.
    
    Args:
        api_key: Submagic API key (or set SUBMAGIC_API_KEY env var)
        
    Returns:
        SubmagicVideoMarketer instance
    """
    if not api_key:
        api_key = os.getenv('SUBMAGIC_API_KEY')
        if not api_key:
            raise ValueError("API key required. Set SUBMAGIC_API_KEY env var or pass api_key parameter.")
    
    return SubmagicVideoMarketer(api_key)

# 🎬 EXAMPLE USAGE FOR DUBAI MARKET
if __name__ == "__main__":
    # Example usage
    api_key = "sk-59c8200945ec78b0e29a400d8d90cdc0c96b5635517dd076f6b2281f7b36fc03"
    client = create_submagic_client(api_key)
    
    # Example 1: Create luxury wellness ad
    project = client.create_luxury_ad(
        title="Dubai Wellness Transformation",
        video_source="https://drive.google.com/your-video.mp4",
        positioning="wellness_transformation"
    )
    
    # Example 2: Create viral clips from YouTube
    clips = client.create_viral_clips_from_youtube(
        youtube_url="https://youtube.com/watch?v=your-video",
        title="Viral Wellness Clips"
    )
    
    # Example 3: Complete workflow
    final_video = client.process_and_download(
        title="Luxury Fitness Ad - Dubai",
        video_source="./raw_video.mp4",
        output_path="./final_luxury_ad.mp4",
        positioning="luxury"
    )
    
    print(f"✅ Final video saved: {final_video}")