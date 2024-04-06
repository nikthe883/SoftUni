from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):

    BUDGET = 5000
    ENGAGEMENT_RATE_MULTIPLIER  = 1.2

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)
    
    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= self.ENGAGEMENT_RATE_MULTIPLIER  * self.required_engagement