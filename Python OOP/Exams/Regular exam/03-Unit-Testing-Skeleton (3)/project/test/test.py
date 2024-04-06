import unittest
from project.social_media import SocialMedia

class TestSocialMedia(unittest.TestCase):

    def setUp(self):
       
        self.social_media = SocialMedia(username="test_user", platform="Instagram", followers=100, content_type="Photo")


    def test_initial_attributes(self):
      
        self.assertEqual(SocialMedia.__base__.__name__, "object")
        self.assertEqual(self.social_media._username, "test_user")
        self.assertEqual(self.social_media.platform, "Instagram")
        self.assertEqual(self.social_media.followers, 100)
        self.assertEqual(self.social_media._content_type, "Photo")
        self.assertEqual(len(self.social_media._posts), 0)


        self.assertTrue(isinstance(getattr(SocialMedia, "platform"), property))
        self.assertTrue(isinstance(getattr(SocialMedia, "followers"), property))


    def test_initialization(self):
        social_media = SocialMedia(username="test_user", platform="Instagram", followers=100, content_type="Photo")

        self.assertEqual(social_media._username, 'test_user')
        self.assertEqual(social_media._platform, 'Instagram')
        self.assertEqual(social_media._followers, 100)
        self.assertEqual(social_media._content_type, "Photo")
        self.assertEqual(social_media._posts, [])



    def test_platform_validation(self):
        valid_platforms = ['Instagram', 'YouTube', 'Twitter']
        for platform in valid_platforms:
            with self.subTest(platform=platform):
                self.social_media.platform = platform
                self.assertEqual(self.social_media.platform, platform)

    def test_platform_validation_invalid(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        invalid_platform = 'InvalidPlatform'
        with self.assertRaises(ValueError) as context:
            self.social_media.platform = invalid_platform
        self.assertEqual(str(context.exception), f"Platform should be one of {allowed_platforms}")

    def test_followers_validation_valid(self):
        self.assertEqual(self.social_media.followers, 100)

    def test_followers_validation_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.social_media.followers = -1
        self.assertEqual(str(context.exception), "Followers cannot be negative.")

    def test_create_post(self):
        result = self.social_media.create_post(post_content="Test Content")
        self.assertIn("New Photo post created by test_user on Instagram.", result)

    def test_like_post(self):
       
        sm = SocialMedia(username="TestUser", platform="Instagram", followers=100, content_type="Photo")
        sm.create_post(post_content="Test Content")
        result = sm.like_post(0)
        self.assertIn("Post liked by TestUser.", result)

    def test_like_post_index_out_of_range(self):
        sm = SocialMedia(username="TestUser", platform="Instagram", followers=100, content_type="Photo")
        sm.create_post(post_content="Test Content")
        result = sm.like_post(1)
        self.assertIn("Invalid post index.", result)

    def test_like_post_max_likes_reached(self):
        sm = SocialMedia(username="TestUser", platform="Instagram", followers=100, content_type="Photo")
        sm.create_post(post_content="Test Content")
        for _ in range(10):
            sm.like_post(0)
        result = sm.like_post(0)
        self.assertIn("Post has reached the maximum number of likes.", result)

    def test_maximum_likes(self):
        sm = SocialMedia(username="TestUser", platform="Instagram", followers=100, content_type="Photo")
        sm.create_post(post_content="Test Content")
        for _ in range(10):
            result = sm.like_post(0)
            self.assertIn("Post liked by TestUser.", result)


    def test_comment_on_post_valid(self):
        
        sm = SocialMedia(username="TestUser", platform="Instagram", followers=100, content_type="Photo")
        sm.create_post(post_content="Test Content")
        result = sm.comment_on_post(post_index=0, comment="This is a valid comment over ten characters.")
        self.assertIn("Comment added by TestUser on the post.", result)

    def test_comment_on_post_empty(self):
        
        sm = SocialMedia(username="TestUser", platform="Instagram", followers=100, content_type="Photo")
        sm.create_post(post_content="Test Content")
        result = sm.comment_on_post(post_index=0, comment="")
        self.assertEqual("Comment should be more than 10 characters.", result)

    def test_comment_on_post_less_than_10_characters(self):
        sm = SocialMedia(username="TestUser", platform="Instagram", followers=100, content_type="Photo")
        sm.create_post(post_content="Test Content")
        result = sm.comment_on_post(post_index=0, comment="Short")
        self.assertEqual("Comment should be more than 10 characters.", result)



if __name__ == '__main__':
    unittest.main()
