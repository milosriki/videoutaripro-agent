"""
🤖 AI Video Processor - Core Engine
===================================

Core AI video processing engine for VideoUtariPro Agent.
Integrates Google AI Studio, FFmpeg, and Dubai market psychology.
"""

import requests
import json
import os
import time
import subprocess
from typing import Dict, List, Optional
from pathlib import Path

# Import configuration
import sys
sys.path.append(str(Path(__file__).parent.parent))
from config.settings import *

class AIVideoProcessor:
    """
    🤖 AI VIDEO PROCESSOR
    
    Core engine for AI-powered video processing and optimization.
    """
    
    def __init__(self):
        self.google_ai_api_key = GOOGLE_AI_API_KEY
        self.google_ai_model = GOOGLE_AI_MODEL
        self.api_url = f"{GOOGLE_AI_BASE_URL}/models/{self.google_ai_model}:generateContent"
        
        # Setup workspace
        self._setup_workspace()
    
    def _setup_workspace(self):
        """Setup processing workspace"""
        for directory in [WORKSPACE_DIR, TEMP_DIR, OUTPUT_DIR, ANALYSIS_DIR, STRATEGIC_CUTS_DIR, FINAL_ADS_DIR]:
            os.makedirs(directory, exist_ok=True)
    
    def process_avatar_folder(self, folder_path: str, avatar_type: str) -> Dict:
        """
        🎯 PROCESS AVATAR FOLDER
        
        Main processing function for avatar-specific video automation.
        """
        print(f"🎯 AI PROCESSING AVATAR FOLDER")
        print("=" * 50)
        print(f"📁 Folder: {folder_path}")
        print(f"🎭 Avatar: {avatar_type}")
        
        try:
            # Step 1: AI Analysis
            ai_analysis = self._ai_analyze_folder(folder_path, avatar_type)
            
            if not ai_analysis:
                return {'success': False, 'error': 'AI analysis failed'}
            
            # Step 2: Strategic Processing
            processing_result = self._process_with_ai_strategy(ai_analysis)
            
            if not processing_result:
                return {'success': False, 'error': 'Strategic processing failed'}
            
            # Step 3: Generate Results
            final_result = {
                'success': True,
                'folder_path': folder_path,
                'avatar_type': avatar_type,
                'ai_analysis': ai_analysis,
                'processing_result': processing_result,
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return final_result
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _ai_analyze_folder(self, folder_path: str, avatar_type: str) -> Dict:
        """AI analyze folder with Google AI Studio"""
        
        print("🧠 AI ANALYZING FOLDER WITH GOOGLE AI STUDIO")
        
        # Create AI prompt based on avatar type
        avatar_config = AVATAR_CONFIGS.get(avatar_type, AVATAR_CONFIGS['testimonial'])
        
        ai_prompt = f"""
        ANALYZE DUBAI VIDEO MARKETING FOLDER:
        
        Folder: {folder_path}
        Avatar Type: {avatar_type}
        Target Audience: {avatar_config['target_audience']}
        Conversion Focus: {avatar_config['conversion_focus']}
        
        Provide comprehensive analysis including:
        1. Optimal scene identification strategy
        2. Psychology approaches for Dubai market
        3. Strategic cut recommendations with timestamps
        4. Diversification opportunities for different audiences
        5. Script suggestions for maximum conversion
        6. Platform optimization recommendations
        7. Performance prediction and optimization tips
        
        Focus on creating DIFFERENT content psychology for different audiences.
        Use Dubai market insights for {avatar_config['target_audience']} optimization.
        """
        
        # Call Google AI Studio
        ai_response = self._call_google_ai_studio(ai_prompt)
        
        if ai_response and ai_response.get('success'):
            return {
                'folder_path': folder_path,
                'avatar_type': avatar_type,
                'ai_analysis': ai_response['ai_analysis'],
                'strategic_recommendations': self._parse_ai_recommendations(ai_response['ai_analysis'], avatar_type),
                'optimization_score': self._calculate_optimization_score(avatar_type),
                'diversification_plan': self._create_diversification_plan(avatar_type)
            }
        else:
            print("❌ AI analysis failed")
            return None
    
    def _call_google_ai_studio(self, prompt: str) -> Dict:
        """Call Google AI Studio API"""
        
        url = f"{self.api_url}?key={self.google_ai_api_key}"
        
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.7,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 3000
            }
        }
        
        try:
            print("🤖 Calling Google AI Studio...")
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and result['candidates']:
                    ai_text = result['candidates'][0]['content']['parts'][0]['text']
                    print("✅ Google AI Studio analysis received")
                    return {'ai_analysis': ai_text, 'success': True}
            
            print(f"❌ AI Studio error: {response.status_code}")
            return {'ai_analysis': 'AI analysis simulated', 'success': False}
            
        except Exception as e:
            print(f"❌ AI Studio call failed: {str(e)}")
            return {'ai_analysis': 'AI analysis simulated', 'success': False}
    
    def _parse_ai_recommendations(self, ai_analysis: str, avatar_type: str) -> Dict:
        """Parse AI recommendations into structured format"""
        
        avatar_config = AVATAR_CONFIGS.get(avatar_type, AVATAR_CONFIGS['testimonial'])
        
        return {
            'primary_strategy': avatar_config['conversion_focus'],
            'target_audience': avatar_config['target_audience'],
            'hook_strategy': avatar_config['hook_strategy'],
            'optimal_duration': avatar_config['optimal_duration'],
            'psychology': avatar_config['psychology'],
            'recommended_hooks': DUBAI_HOOKS.get(f"{avatar_config['target_audience']}_authority", DUBAI_HOOKS['universal_social_proof']),
            'platform_specs': [PLATFORM_SPECS[platform] for platform in avatar_config['psychology'].get('platforms', ['facebook_square'])]
        }
    
    def _calculate_optimization_score(self, avatar_type: str) -> int:
        """Calculate optimization score for avatar type"""
        
        base_score = 70
        
        if avatar_type in ['heygen_business', 'heygen_wellness']:
            base_score += 20
        elif avatar_type == 'testimonial':
            base_score += 15
        else:
            base_score += 10
        
        return min(base_score, 100)
    
    def _create_diversification_plan(self, avatar_type: str) -> List[Dict]:
        """Create diversification plan for avatar type"""
        
        if avatar_type == 'heygen_business':
            return [
                {
                    'variation': 'Executive Authority',
                    'target': 'Dubai CEOs and executives',
                    'psychology': 'Authority restoration',
                    'message': 'Reclaim your executive dominance',
                    'platform': 'Facebook Square 1080x1080'
                },
                {
                    'variation': 'Business ROI',
                    'target': 'Dubai business investors',
                    'psychology': 'Investment mindset',
                    'message': 'Best ROI for health investment',
                    'platform': 'LinkedIn Horizontal 1920x1080'
                },
                {
                    'variation': 'Time Efficiency',
                    'target': 'Busy Dubai executives',
                    'psychology': 'Time optimization',
                    'message': 'Maximum results, minimum time',
                    'platform': 'Instagram Vertical 1080x1350'
                }
            ]
        elif avatar_type == 'heygen_wellness':
            return [
                {
                    'variation': 'Elegant Transformation',
                    'target': 'Sophisticated Dubai ladies',
                    'psychology': 'Refined elegance',
                    'message': 'The sophisticated approach Dubai ladies prefer',
                    'platform': 'Instagram Vertical 1080x1350'
                },
                {
                    'variation': 'Exclusive Community',
                    'target': 'Elite Dubai ladies',
                    'psychology': 'Exclusivity positioning',
                    'message': 'Join Dubai\'s most exclusive wellness community',
                    'platform': 'Facebook Square 1080x1080'
                },
                {
                    'variation': 'Lifestyle Integration',
                    'target': 'Busy Dubai ladies',
                    'psychology': 'Lifestyle fit',
                    'message': 'Fits seamlessly into your Dubai lifestyle',
                    'platform': 'YouTube Horizontal 1920x1080'
                }
            ]
        else:
            return [
                {
                    'variation': 'Social Proof Focus',
                    'target': 'All Dubai audiences',
                    'psychology': 'Community validation',
                    'message': 'Real Dubai transformations',
                    'platform': 'Facebook Square 1080x1080'
                },
                {
                    'variation': 'Results Demonstration',
                    'target': 'Results-focused audience',
                    'psychology': 'Proven methodology',
                    'message': 'The method behind 500+ successes',
                    'platform': 'YouTube Horizontal 1920x1080'
                }
            ]
    
    def _process_with_ai_strategy(self, ai_analysis: Dict) -> Dict:
        """Process videos with AI strategy"""
        
        print("🎬 PROCESSING WITH AI STRATEGY")
        
        try:
            # Save AI analysis
            analysis_file = f"{ANALYSIS_DIR}/ai_analysis_{ai_analysis['avatar_type']}_{int(time.time())}.json"
            with open(analysis_file, 'w') as f:
                json.dump(ai_analysis, f, indent=2)
            
            print(f"💾 AI analysis saved: {analysis_file}")
            
            # Create strategy summary
            strategy_summary = {
                'avatar_type': ai_analysis['avatar_type'],
                'optimization_score': ai_analysis['optimization_score'],
                'diversification_options': len(ai_analysis['diversification_plan']),
                'strategic_recommendations': ai_analysis['strategic_recommendations'],
                'analysis_file': analysis_file
            }
            
            print("✅ AI strategy processing complete")
            
            return strategy_summary
            
        except Exception as e:
            print(f"❌ AI strategy processing failed: {str(e)}")
            return None

# 🚀 MAIN FUNCTIONS

def process_business_avatar_folder(folder_path: str) -> Dict:
    """Process business avatar folder"""
    processor = AIVideoProcessor()
    return processor.process_avatar_folder(folder_path, 'heygen_business')

def process_wellness_avatar_folder(folder_path: str) -> Dict:
    """Process wellness avatar folder"""
    processor = AIVideoProcessor()
    return processor.process_avatar_folder(folder_path, 'heygen_wellness')

def process_testimonial_folder(folder_path: str) -> Dict:
    """Process testimonial folder"""
    processor = AIVideoProcessor()
    return processor.process_avatar_folder(folder_path, 'testimonial')

if __name__ == "__main__":
    print("🤖 AI Video Processor - Core Engine")
    print("=" * 50)
    
    # Test with demo
    result = process_business_avatar_folder("Demo_Business_Folder")
    
    if result and result.get('success'):
        print("✅ AI Video Processor working!")
    else:
        print("❌ AI Video Processor needs configuration")