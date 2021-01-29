require 'csv'

class ApplicationController < ActionController::Base
  # protect_from_forgery with: :null_session
  skip_before_action :verify_authenticity_token

  def current_user
    User.where(id: session[:user_id]).first
  end

  helper_method :current_user
end
