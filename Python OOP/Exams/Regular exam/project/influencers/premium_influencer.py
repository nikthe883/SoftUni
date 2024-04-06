from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign

class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.85  

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:
    
        return campaign.budget * PremiumInfluencer.PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str) -> int:
        
        multiplier = 1.5 if campaign_type == "HighBudgetCampaign" else 0.8
        return int(self.followers * self.engagement_rate * multiplier)
