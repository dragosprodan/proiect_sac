require 'test_helper'

class HomeControllerTest < ActionDispatch::IntegrationTest
  test "should get home" do
    get home_home_url
    assert_response :success
  end

  test "should get welcome" do
    get home_welcome_url
    assert_response :success
  end

  test "should get test_area" do
    get home_test_area_url
    assert_response :success
  end

end
