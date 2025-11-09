"""
🎯 Dubai Creative Strategist - Complete System
==============================================

Complete Dubai video creative strategist system integrating:
- Google AI Studio for intelligent analysis
- FFmpeg for professional video processing
- Dubai market psychology frameworks
- Alan Sultanic conversion methodologies

Agent ID: 6ec0aeac-5d39-4585-905d-8e77a15120d0
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

class DubaiCreativeStrategist:
    """
    🎯 DUBAI CREATIVE STRATEGIST
    
    Complete creative strategist system for Dubai video marketing.
    """
    
    def __init__(self):
        self.agent_id = DUBAI_AGENT_ID
        self.google_ai_api_key = GOOGLE_AI_API_KEY
        self.google_ai_model = GOOGLE_AI_MODEL
        self.api_url = f"{GOOGLE_AI_BASE_URL}/models/{self.google_ai_model}:generateContent"
        
        # Setup workspace
        self._setup_workspace()
        
        # Dubai market psychology frameworks
        self.psychology_frameworks = {
            'authority_restoration': {
                'target': 'Dubai men 40+ executives',
                'triggers': ['lost_dominance', 'competitive_pressure', 'executive_decline'],
                'messaging': 'Reclaim your executive edge',
                'hooks': DUBAI_HOOKS['men_40_authority'],
                'optimal_scenes': ['authority_establishment', 'problem_agitation', 'solution_reveal', 'social_proof_cta']
            },
            'elegant_transformation': {
                'target': 'Dubai women 40+ sophisticated',
                'triggers': ['refined_approach', 'exclusive_community', 'elegant_results'],
                'messaging': 'Sophisticated transformation approach',
                'hooks': DUBAI_HOOKS['women_40_elegant'],
                'optimal_scenes': ['elegant_introduction', 'lifestyle_integration', 'transformation_story', 'exclusive_invitation']
            },
            'social_proof_validation': {
                'target': 'All Dubai audiences',
                'triggers': ['community_success', 'real_results', 'proven_method'],
                'messaging': 'Join successful Dubai community',
                'hooks': DUBAI_HOOKS['universal_social_proof'],
                'optimal_scenes': ['results_hook', 'success_stories', 'community_proof', 'join_cta']
            }
        }
    
    def _setup_workspace(self):
        """Setup creative strategist workspace"""
        for directory in [WORKSPACE_DIR, TEMP_DIR, OUTPUT_DIR, ANALYSIS_DIR, STRATEGIC_CUTS_DIR, FINAL_ADS_DIR]:
            os.makedirs(directory, exist_ok=True)
    
    def analyze_and_strategize(self, folder_path: str, avatar_type: str) -> Dict:
        """
        🧠 ANALYZE AND STRATEGIZE
        
        Complete analysis and strategic planning for Dubai market.
        """
        print("🧠 DUBAI CREATIVE STRATEGIST - ANALYSIS & STRATEGY")
        print("=" * 60)
        print(f"🎭 Avatar: {avatar_type}")
        print(f"📁 Folder: {folder_path}")
        
        try:
            # Get avatar configuration
            avatar_config = AVATAR_CONFIGS.get(avatar_type, AVATAR_CONFIGS['testimonial'])
            psychology_framework = self.psychology_frameworks.get(
                avatar_config['psychology']['primary'], 
                self.psychology_frameworks['social_proof_validation']
            )
            
            print(f"🎯 Target: {psychology_framework['target']}")
            print(f"🧠 Psychology: {avatar_config['psychology']['primary']}")
            print(f"💬 Messaging: {psychology_framework['messaging']}")
            
            # Create comprehensive AI prompt
            strategic_prompt = self._create_strategic_ai_prompt(folder_path, avatar_type, psychology_framework)
            
            # Get AI strategic analysis
            ai_response = self._call_google_ai_studio(strategic_prompt)
            
            if ai_response and ai_response.get('success'):
                # Process AI response into strategic plan
                strategic_plan = {
                    'agent_id': self.agent_id,
                    'folder_path': folder_path,
                    'avatar_type': avatar_type,
                    'target_audience': psychology_framework['target'],
                    'psychology_framework': psychology_framework,
                    'ai_strategic_analysis': ai_response['ai_analysis'],
                    'recommended_scenes': psychology_framework['optimal_scenes'],
                    'recommended_hooks': psychology_framework['hooks'],
                    'diversification_strategy': self._create_diversification_strategy(avatar_type),
                    'platform_optimization': self._create_platform_optimization(avatar_type),
                    'performance_prediction': self._predict_performance(avatar_type),
                    'implementation_plan': self._create_implementation_plan(avatar_type)
                }
                
                # Save strategic plan
                strategy_file = self._save_strategic_plan(strategic_plan)
                strategic_plan['strategy_file'] = strategy_file
                
                print("✅ Strategic analysis complete!")
                print(f"📋 Strategy saved: {strategy_file}")
                print(f"🎯 Scenes: {len(strategic_plan['recommended_scenes'])}")
                print(f"🎨 Diversification: {len(strategic_plan['diversification_strategy'])}")
                print(f"📈 Performance: {strategic_plan['performance_prediction']}")
                
                return strategic_plan
            else:
                print("❌ AI strategic analysis failed")
                return None
                
        except Exception as e:
            print(f"❌ Strategic analysis error: {str(e)}")
            return None
    
    def _create_strategic_ai_prompt(self, folder_path: str, avatar_type: str, psychology_framework: Dict) -> str:
        """Create strategic AI prompt"""
        
        return f"""
        DUBAI CREATIVE STRATEGIST ANALYSIS:
        
        Project: VideoUtariPro Agent
        Folder: {folder_path}
        Avatar Type: {avatar_type}
        Target Audience: {psychology_framework['target']}
        Psychology Framework: {psychology_framework['triggers']}
        
        As a professional creative strategist specializing in Dubai market video marketing,
        analyze this {avatar_type} content and provide:
        
        1. SCENE OPTIMIZATION STRATEGY:
        - Identify optimal scenes for {psychology_framework['target']}
        - Recommend specific timestamps for maximum impact
        - Suggest psychology-based scene sequencing
        - Provide editing recommendations for each scene
        
        2. DUBAI MARKET PSYCHOLOGY:
        - Apply {psychology_framework['messaging']} positioning
        - Use cultural insights for Dubai audience 40+
        - Integrate Alan Sultanic conversion frameworks
        - Focus on {', '.join(psychology_framework['triggers'])} triggers
        
        3. DIVERSIFICATION STRATEGY:
        - Create multiple variations for different sub-audiences
        - Recommend platform-specific optimizations
        - Suggest A/B testing approaches
        - Provide performance optimization tips
        
        4. SCRIPT RECOMMENDATIONS:
        - Provide Dubai-specific hooks and messaging
        - Create audience-specific value propositions
        - Develop compelling calls-to-action
        - Integrate social proof elements
        
        5. IMPLEMENTATION ROADMAP:
        - Prioritize scenes by conversion potential
        - Recommend production sequence
        - Suggest testing and optimization approach
        - Provide scaling recommendations
        
        Focus on creating DIFFERENT content psychology for different audiences within the Dubai market.
        Ensure recommendations are actionable and specific to {avatar_type} content optimization.
        """
    
    def _call_google_ai_studio(self, prompt: str) -> Dict:
        """Call Google AI Studio for strategic analysis"""
        
        url = f"{self.api_url}?key={self.google_ai_api_key}"
        
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.8,  # Higher creativity for strategic planning
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 4000  # More tokens for comprehensive strategy
            }
        }
        
        try:
            print("🎯 Calling Google AI Studio for strategic analysis...")
            response = requests.post(url, headers=headers, json=payload, timeout=90)
            
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and result['candidates']:
                    ai_text = result['candidates'][0]['content']['parts'][0]['text']
                    print("✅ Strategic analysis received from Google AI Studio")
                    return {'ai_analysis': ai_text, 'success': True}
            
            print(f"❌ AI Studio strategic analysis error: {response.status_code}")
            return {'ai_analysis': 'Strategic analysis simulated', 'success': False}
            
        except Exception as e:
            print(f"❌ AI Studio strategic call failed: {str(e)}")
            return {'ai_analysis': 'Strategic analysis simulated', 'success': False}
    
    def _create_diversification_strategy(self, avatar_type: str) -> List[Dict]:
        """Create comprehensive diversification strategy"""
        
        avatar_config = AVATAR_CONFIGS.get(avatar_type, AVATAR_CONFIGS['testimonial'])
        
        base_variations = []
        
        if avatar_type == 'heygen_business':
            base_variations = [
                {'name': 'Executive Authority', 'focus': 'Leadership positioning', 'audience': 'Dubai CEOs'},
                {'name': 'Business ROI', 'focus': 'Investment returns', 'audience': 'Dubai investors'},
                {'name': 'Competitive Edge', 'focus': 'Market advantage', 'audience': 'Dubai executives'},
                {'name': 'Time Optimization', 'focus': 'Efficiency focus', 'audience': 'Busy professionals'}
            ]
        elif avatar_type == 'heygen_wellness':
            base_variations = [
                {'name': 'Elegant Transformation', 'focus': 'Sophisticated wellness', 'audience': 'Refined ladies'},
                {'name': 'Exclusive Community', 'focus': 'Elite membership', 'audience': 'Elite Dubai women'},
                {'name': 'Lifestyle Integration', 'focus': 'Seamless fit', 'audience': 'Busy Dubai ladies'},
                {'name': 'Premium Experience', 'focus': 'Luxury wellness', 'audience': 'High-end market'}
            ]
        else:
            base_variations = [
                {'name': 'Social Proof', 'focus': 'Community validation', 'audience': 'All audiences'},
                {'name': 'Results Focus', 'focus': 'Proven outcomes', 'audience': 'Results-driven'},
                {'name': 'Community Success', 'focus': 'Group achievement', 'audience': 'Community-minded'}
            ]
        
        # Enhance with psychology and platform optimization
        enhanced_variations = []
        for variation in base_variations:
            enhanced_variations.append({
                **variation,
                'psychology': avatar_config['psychology']['primary'],
                'conversion_focus': avatar_config['conversion_focus'],
                'optimal_platforms': avatar_config['psychology'].get('platforms', ['facebook_square']),
                'recommended_duration': avatar_config['optimal_duration']
            })
        
        return enhanced_variations
    
    def _create_platform_optimization(self, avatar_type: str) -> Dict:
        """Create platform optimization recommendations"""
        
        avatar_config = AVATAR_CONFIGS.get(avatar_type, AVATAR_CONFIGS['testimonial'])
        platforms = avatar_config['psychology'].get('platforms', ['facebook_square'])
        
        optimization = {}
        
        for platform in platforms:
            if platform in PLATFORM_SPECS:
                specs = PLATFORM_SPECS[platform]
                optimization[platform] = {
                    'specs': specs,
                    'optimization_tips': self._get_platform_tips(platform, avatar_type),
                    'psychology_adaptation': self._get_psychology_adaptation(platform, avatar_type)
                }
        
        return optimization
    
    def _get_platform_tips(self, platform: str, avatar_type: str) -> List[str]:
        """Get platform-specific optimization tips"""
        
        tips = {
            'facebook_square': [
                'Use square format for maximum feed visibility',
                'Add captions for silent autoplay',
                'Include clear CTA in first 3 seconds',
                'Optimize for mobile viewing'
            ],
            'instagram_vertical': [
                'Use vertical format for Stories and Reels',
                'Add engaging visual elements',
                'Include trending hashtags',
                'Optimize for quick consumption'
            ],
            'youtube_horizontal': [
                'Use horizontal format for desktop viewing',
                'Create compelling thumbnails',
                'Add detailed descriptions',
                'Optimize for search discovery'
            ],
            'linkedin_horizontal': [
                'Use professional horizontal format',
                'Focus on business value proposition',
                'Include industry-specific messaging',
                'Optimize for professional audience'
            ]
        }
        
        return tips.get(platform, ['Standard optimization recommendations'])
    
    def _get_psychology_adaptation(self, platform: str, avatar_type: str) -> str:
        """Get psychology adaptation for platform"""
        
        adaptations = {
            'facebook_square': 'Authority positioning with social proof elements',
            'instagram_vertical': 'Lifestyle integration with visual appeal',
            'youtube_horizontal': 'Educational authority with detailed methodology',
            'linkedin_horizontal': 'Professional credibility with business focus'
        }
        
        return adaptations.get(platform, 'Standard psychology approach')
    
    def _predict_performance(self, avatar_type: str) -> str:
        """Predict performance for avatar type"""
        
        predictions = {
            'heygen_business': 'Very High - Strong authority positioning for Dubai executives',
            'heygen_wellness': 'Very High - Elegant appeal for sophisticated Dubai ladies',
            'testimonial': 'High - Authentic social proof for all audiences',
            'teaching': 'Medium-High - Educational authority for mixed audiences'
        }
        
        return predictions.get(avatar_type, 'Medium - Standard performance expected')
    
    def _create_implementation_plan(self, avatar_type: str) -> Dict:
        """Create implementation plan"""
        
        avatar_config = AVATAR_CONFIGS.get(avatar_type, AVATAR_CONFIGS['testimonial'])
        
        return {
            'phase_1': {
                'name': 'AI Analysis & Strategic Planning',
                'duration': '1-2 hours',
                'tasks': [
                    'Analyze video content with Google AI Studio',
                    'Identify optimal scenes and timestamps',
                    'Create psychology-based strategy',
                    'Plan diversification approach'
                ]
            },
            'phase_2': {
                'name': 'Strategic Video Processing',
                'duration': '2-4 hours',
                'tasks': [
                    'Extract strategic cuts with FFmpeg',
                    'Apply Dubai market psychology',
                    'Create audience-specific variations',
                    'Optimize for target platforms'
                ]
            },
            'phase_3': {
                'name': 'Testing & Optimization',
                'duration': '1-2 weeks',
                'tasks': [
                    'A/B test different variations',
                    'Monitor conversion performance',
                    'Optimize based on results',
                    'Scale successful combinations'
                ]
            },
            'success_metrics': {
                'ai_optimization_score': '85+ out of 100',
                'audience_engagement': 'High for target demographics',
                'conversion_potential': avatar_config['conversion_focus'],
                'dubai_market_fit': 'Optimized for cultural preferences'
            }
        }
    
    def _save_strategic_plan(self, strategic_plan: Dict) -> str:
        """Save strategic plan to file"""
        
        strategy_file = f"{ANALYSIS_DIR}/dubai_strategy_{strategic_plan['avatar_type']}_{int(time.time())}.json"
        
        with open(strategy_file, 'w') as f:
            json.dump(strategic_plan, f, indent=2)
        
        # Also create markdown summary
        md_file = strategy_file.replace('.json', '.md')
        with open(md_file, 'w') as f:
            f.write(f"# 🎯 Dubai Creative Strategy: {strategic_plan['avatar_type'].upper()}\n\n")
            f.write(f"**Agent ID**: {strategic_plan['agent_id']}\n")
            f.write(f"**Target**: {strategic_plan['target_audience']}\n")
            f.write(f"**Psychology**: {strategic_plan['psychology_framework']['messaging']}\n")
            f.write(f"**Performance**: {strategic_plan['performance_prediction']}\n\n")
            f.write("## 🤖 AI Strategic Analysis\n\n")
            f.write(strategic_plan['ai_strategic_analysis'])
            f.write("\n\n## 🎬 Recommended Scenes\n\n")
            for i, scene in enumerate(strategic_plan['recommended_scenes']):
                f.write(f"{i+1}. **{scene.replace('_', ' ').title()}**\n")
            f.write("\n\n## 🎯 Diversification Strategy\n\n")
            for i, strategy in enumerate(strategic_plan['diversification_strategy']):
                f.write(f"{i+1}. **{strategy['name']}**: {strategy['focus']} - {strategy['audience']}\n")
        
        return md_file
    
    def create_complete_dubai_strategy(self, folder_path: str, avatar_type: str) -> Dict:
        """
        🎯 CREATE COMPLETE DUBAI STRATEGY
        
        Main function for complete strategic analysis and planning.
        """
        print("🎯 CREATING COMPLETE DUBAI STRATEGY")
        print("=" * 60)
        
        try:
            # Run complete analysis and strategizing
            strategic_plan = self.analyze_and_strategize(folder_path, avatar_type)
            
            if strategic_plan:
                print(f"\n📊 STRATEGIC PLAN SUMMARY:")
                print("=" * 50)
                print(f"🎭 Avatar: {strategic_plan['avatar_type']}")
                print(f"👥 Target: {strategic_plan['target_audience']}")
                print(f"🧠 Psychology: {strategic_plan['psychology_framework']['messaging']}")
                print(f"📈 Performance: {strategic_plan['performance_prediction']}")
                print(f"🎬 Scenes: {len(strategic_plan['recommended_scenes'])}")
                print(f"🎨 Variations: {len(strategic_plan['diversification_strategy'])}")
                print(f"📋 Strategy File: {strategic_plan['strategy_file']}")
                
                return {
                    'success': True,
                    'strategic_plan': strategic_plan,
                    'agent_id': self.agent_id
                }
            else:
                return {'success': False, 'error': 'Strategic planning failed'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}

# 🚀 MAIN STRATEGIST FUNCTIONS

def create_business_strategy(folder_path: str) -> Dict:
    """Create business avatar strategy"""
    strategist = DubaiCreativeStrategist()
    return strategist.create_complete_dubai_strategy(folder_path, 'heygen_business')

def create_wellness_strategy(folder_path: str) -> Dict:
    """Create wellness avatar strategy"""
    strategist = DubaiCreativeStrategist()
    return strategist.create_complete_dubai_strategy(folder_path, 'heygen_wellness')

def create_testimonial_strategy(folder_path: str) -> Dict:
    """Create testimonial strategy"""
    strategist = DubaiCreativeStrategist()
    return strategist.create_complete_dubai_strategy(folder_path, 'testimonial')

if __name__ == "__main__":
    print("🎯 Dubai Creative Strategist - Complete System")
    print("=" * 60)
    
    # Test with demo
    result = create_business_strategy("Demo_Business_Folder")
    
    if result and result.get('success'):
        print("✅ Dubai Creative Strategist working!")
        print(f"🤖 Agent ID: {result['agent_id']}")
    else:
        print("❌ Dubai Creative Strategist needs configuration")