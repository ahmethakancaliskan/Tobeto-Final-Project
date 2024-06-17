from pages.member_communuties_page import MemberCommunitiesPage
from tests.base_test import BaseTest
from constants.member_communuties_page_constants import MemberCommunutiesPageConstants


class TestMemberCommunutiesPage(BaseTest):
    #Case 1: Başarılı topluluk ekleme Kontrolü
    def test_add_community_succesfully(self):
        member_communities_page = MemberCommunitiesPage(self.driver)
        member_communities_page.precondition()
        member_communities_page.enter_communutiy_name("Galatasaraylılar Derneği")
        member_communities_page.enter_role("Taraftar")
        member_communities_page.click_save_button()
        assert member_communities_page.get_warning_massage() == MemberCommunutiesPageConstants.VALID

    def test_already_added(self):
        member_communities_page = MemberCommunitiesPage(self.driver)
        member_communities_page.precondition()
        member_communities_page.enter_communutiy_name("Galatasaraylılar Derneği")
        member_communities_page.enter_role("Taraftar")
        member_communities_page.click_save_button()
        assert member_communities_page.get_warning_massage() == MemberCommunutiesPageConstants.ALREADY_ADDED
