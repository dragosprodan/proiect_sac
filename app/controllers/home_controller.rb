class HomeController < ApplicationController
  def home
    @current_user = current_user
    @user = current_user
    @list_of_files = Dir.entries("public/uploads/" + current_user.id.to_s + "_files").drop(1)
    @list_of_files.delete("output")
  end

  def login
  end

  def register
  end

  def welcome
    @current_user = current_user
    if current_user != nil
      history_list = UserHistory.where(id_user: @current_user.id).all.map{|p|p.id_essay}
      @essay_history = Essay.where(id: history_list)
    end

  end

  def test_area
  end

  def upload
    uploaded_file = params[:audio]
    if params[:id].to_s == current_user.id.to_s
      File.open(Rails.root.join('public', 'uploads', current_user.id.to_s + '_files', uploaded_file.original_filename), 'wb') do |file|
        file.write(uploaded_file.read)
        redirect_to home_path
      end
    end

  end

  def recommend
    @current_user = current_user
    score = UserScore.where(id_user: @current_user.id).first
    @similar_essays = Essay.where(:score => (score.score)..(score.score + 10)).shuffle[0..4]

  end

  def delete_upload
    uploaded_file = params[:audio_name]
    path_to_file = "public/uploads/" + current_user.id.to_s + "_files/" + uploaded_file
    File.delete(path_to_file) if File.exist?(path_to_file)
    redirect_to home_path
  end

  def import_data
    # Essay.delete_all
    # parsed_file = CSV.read("app/assets/python/data/out.csv", :headers => true)
    # for elem in parsed_file do
    #   data = Essay.new
    #   data.data = elem["essay"].to_s
    #   data.score = elem["domain1_score"].to_s.to_i
    #   data.save
    # end
  end
end
