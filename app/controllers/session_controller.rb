class SessionController < ApplicationController

  def login
    user = find_user
    if not user.nil? and user.authenticate(params[:password])
      session[:user_id] = user.id
      redirect_to root_path
    else
      redirect_to login_path
    end
  end

  def register
    if verify_params_register
      user = User.new
      user.name = params[:name]
      user.email = params[:email]
      user.username = params[:username]
      user.password = params[:password]
      user.save

      score = UserScore.new
      score.id_user= user.id
      score.score= 0
      score.save

      Dir.mkdir('public/uploads/' + user.id.to_s + '_files')
      Dir.mkdir('public/uploads/' + user.id.to_s + '_files/' + 'output')

      session[:user_id] = user.id
      redirect_to root_path
    else
      redirect_to register_path
    end
  end

  def logout
    session[:user_id] = nil
    redirect_to root_path
  end

  private

  def find_user
    if params[:username] != ""
      return User.find_by(username: params[:username])
    end

    nil
  end

  def verify_params_register
    if params[:email] == "" or not params[:email].include? "@"
      return false
    end

    if params[:password] == "" or params[:password].length < 4
      return false
    end

    if params[:username] == "" or params[:username].length < 4
      return false
    end

    if params[:name] == ""
      return false
    end

    true
  end

end
