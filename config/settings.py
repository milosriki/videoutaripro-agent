"""
🔧 VideoUtariPro Agent Configuration
===================================

Configuration settings for AI video marketing automation.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Google AI Studio Configuration
GOOGLE_AI_API_KEY = "AIzaSyBO7VxTMzC-_ZKNbf-4WQN87fje7mmgdT0"
GOOGLE_AI_MODEL = "gemini-2.5-flash"
GOOGLE_AI_BASE_URL = "https://generativelanguage.googleapis.com/v1"

# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT = "norse-acrobat-313613"
GOOGLE_CLOUD_ACCOUNT = "milos@personaltrainersdubai.com"

# Submagic API Configuration
SUBMAGIC_API_KEY = "sk-6d00407fa9e263223d55834e93e1b7d996fe2c6781d8644098bcde82d996e1d4"
SUBMAGIC_BASE_URL = "https://api.submagic.co/v1"

# Dubai Video Creative Strategist Agent
DUBAI_AGENT_ID = "6ec0aeac-5d39-4585-905d-8e77a15120d0"

# Video Processing Settings
DEFAULT_VIDEO_QUALITY = "high"
DEFAULT_OUTPUT_FORMAT = "mp4"
MAX_VIDEO_DURATION = 300  # 5 minutes
MIN_VIDEO_DURATION = 10   # 10 seconds

# Dubai Market Psychology Settings
DUBAI_MEN_40_PSYCHOLOGY = {
    'primary': 'authority_restoration',
    'secondary': 'competitive_edge_recovery',
    'messaging': 'executive_dominance',
    'platforms': ['facebook_square', 'linkedin_horizontal', 'instagram_vertical']
}

DUBAI_WOMEN_40_PSYCHOLOGY = {
    'primary': 'elegant_transformation',
    'secondary': 'exclusive_community',
    'messaging': 'sophisticated_wellness',
    'platforms': ['instagram_vertical', 'facebook_square', 'youtube_horizontal']
}

# Avatar Type Configurations
AVATAR_CONFIGS = {
    'heygen_business': {
        'target_audience': 'dubai_men_40',
        'psychology': DUBAI_MEN_40_PSYCHOLOGY,
        'optimal_duration': 30,
        'hook_strategy': 'authority_positioning',
        'conversion_focus': 'executive_credibility'
    },
    'heygen_wellness': {
        'target_audience': 'dubai_women_40',
        'psychology': DUBAI_WOMEN_40_PSYCHOLOGY,
        'optimal_duration': 30,
        'hook_strategy': 'elegant_positioning',
        'conversion_focus': 'sophisticated_transformation'
    },
    'testimonial': {
        'target_audience': 'all_audiences',
        'psychology': {'primary': 'social_proof', 'secondary': 'community_validation'},
        'optimal_duration': 25,
        'hook_strategy': 'results_positioning',
        'conversion_focus': 'trust_building'
    },
    'teaching': {
        'target_audience': 'mixed_audience',
        'psychology': {'primary': 'authority_building', 'secondary': 'knowledge_demonstration'},
        'optimal_duration': 35,
        'hook_strategy': 'expertise_positioning',
        'conversion_focus': 'educational_authority'
    }
}

# Platform Specifications
PLATFORM_SPECS = {
    'facebook_square': {'width': 1080, 'height': 1080, 'fps': 30, 'bitrate': '2M'},
    'instagram_vertical': {'width': 1080, 'height': 1350, 'fps': 30, 'bitrate': '2.5M'},
    'youtube_horizontal': {'width': 1920, 'height': 1080, 'fps': 30, 'bitrate': '3M'},
    'linkedin_horizontal': {'width': 1920, 'height': 1080, 'fps': 30, 'bitrate': '2.5M'},
    'tiktok_vertical': {'width': 1080, 'height': 1920, 'fps': 30, 'bitrate': '2M'}
}

# File Paths
WORKSPACE_DIR = "./videoutaripro_workspace"
TEMP_DIR = f"{WORKSPACE_DIR}/temp"
OUTPUT_DIR = f"{WORKSPACE_DIR}/output"
ANALYSIS_DIR = f"{WORKSPACE_DIR}/analysis"
STRATEGIC_CUTS_DIR = f"{WORKSPACE_DIR}/strategic_cuts"
FINAL_ADS_DIR = f"{WORKSPACE_DIR}/final_ads"

# Processing Settings
FFMPEG_PRESET = "fast"
FFMPEG_CRF = "23"  # High quality
PROCESSING_TIMEOUT = 120  # 2 minutes per operation
BATCH_SIZE = 5  # Process 5 videos at a time

# Dubai Market Hooks
DUBAI_HOOKS = {
    'men_40_authority': [
        "Dubai executives remember when they dominated both boardroom AND gym...",
        "Why Dubai's top CEOs choose this over expensive personal trainers...",
        "The secret Dubai's most successful businessmen use to stay competitive...",
        "Reclaim your executive edge with the proven methodology...",
        "500+ Dubai executives have transformed their performance..."
    ],
    'women_40_elegant': [
        "Sophisticated Dubai ladies discovered this elegant transformation approach...",
        "Dubai's most discerning women prefer this refined wellness method...",
        "The exclusive approach Dubai's elite ladies use for lasting results...",
        "Join Dubai's most sophisticated wellness community...",
        "Experience the transformation Dubai's refined ladies love..."
    ],
    'universal_social_proof': [
        "500+ Dubai residents can't be wrong about these incredible results...",
        "The transformation method taking Dubai by storm...",
        "Real Dubai success stories that will inspire you...",
        "Join the growing Dubai transformation community...",
        "Proven results from real Dubai clients just like you..."
    ]
}

# Performance Optimization
OPTIMIZATION_SETTINGS = {
    'enable_ai_analysis': True,
    'enable_strategic_cuts': True,
    'enable_diversification': True,
    'enable_batch_processing': True,
    'enable_performance_tracking': True,
    'enable_automatic_upload': True
}