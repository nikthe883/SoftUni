from project.influencers.standard_influencer import StandardInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign



class InfluencerManagerApp:

    INFLUENCERS = ["PremiumInfluencer", "StandardInfluencer"]
    CAMPAIGNS =  ["HighBudgetCampaign", "LowBudgetCampaign"]

    def __init__(self) -> None:
        self.influencers = []
        self.campaigns = []


    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
    
        if influencer_type not in self.INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."
        
        if any(influencer.username == username for influencer in self.influencers):
            return f"{username} is already registered."
        
        influencer = None
        if influencer_type == "PremiumInfluencer":
            
            influencer = PremiumInfluencer(username, followers, engagement_rate)

        elif influencer_type == "StandardInfluencer":
            
            influencer = StandardInfluencer(username, followers, engagement_rate)
        
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."
    

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):

        if campaign_type not in self.CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."
        
        if any(campaign.campaign_id == campaign_id for campaign in self.campaigns):
            return f"Campaign ID {campaign_id} has already been created."
        
        campaign = None
        if campaign_type == "HighBudgetCampaign":
            
            campaign = HighBudgetCampaign(campaign_id, brand, required_engagement)
        elif campaign_type == "LowBudgetCampaign":
            
            campaign = LowBudgetCampaign(campaign_id, brand, required_engagement)
        
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."
    


    def participate_in_campaign(self, influencer_username: str, campaign_id: int):

        influencer = next((influencer for influencer in self.influencers if influencer.username == influencer_username), None)
        campaign = next((campaign for campaign in self.campaigns if campaign.campaign_id == campaign_id), None)
        
        if not influencer:
            return f"Influencer '{influencer_username}' not found."
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."
        
        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        
        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment  
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."
        
    

    def calculate_total_reached_followers(self):
        total_reached_followers = {}

        for campaign in self.campaigns:
            total_for_campaign = 0
            for influencer in self.influencers:
                if campaign in influencer.campaigns_participated:
                    total_for_campaign += influencer.reached_followers(campaign.__class__.__name__)

       
            if total_for_campaign > 0:
                total_reached_followers[campaign] = total_for_campaign

        return total_reached_followers
    

    def influencer_campaign_report(self, username: str):
        influencer = next((influencer for influencer in self.influencers if influencer.username == username), None)
        
        campaign_messages = []
        for campaign in influencer.campaigns_participated:
            reached_followers = influencer.reached_followers(campaign.__class__.__name__)
            campaign_messages.append(f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {reached_followers}")
        
        if not campaign_messages:
            return f"{username} has not participated in any campaigns."
        else:
            return f"{type(influencer).__name__} :) {username} :) participated in the following campaigns:\n" + "\n".join(campaign_messages)
        


    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        stats_messages = ["$$ Campaign Statistics $$"]
        for campaign in sorted_campaigns:
            total_followers = sum(influencer.reached_followers(campaign.__class__.__name__)
                                  for influencer in campaign.approved_influencers)
            stats_messages.append(f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_followers}")
        return "\n".join(stats_messages)