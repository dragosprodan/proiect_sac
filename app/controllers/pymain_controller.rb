class PymainController < ApplicationController
  def run_stt
    user_id = current_user.id
    python_cmd = Escape.shell_command(['python', Rails.root.join('app/assets/python/test.py').to_s, user_id.to_s, params[:filename].to_s ]).to_s
    escape_run python_cmd

    redirect_to edit_text_path
  end

  def edit_text
    @current_user = current_user
    file = File.open "public/uploads/" + current_user.id.to_s + "_files/output/testfile.txt"
    @text_data = file.read
    file.close
  end

  def run_ta
    @current_user = current_user
    user_id = current_user.id

    file = File.open "public/uploads/" + user_id.to_s + "_files/output/testfile.txt", 'w'
    file.write params[:text_data]
    file.close

    python_cmd = Escape.shell_command([Rails.root.join('app/assets/python/test2.py').to_s, user_id.to_s, 'testfile.txt' ]).to_s
    python_cmd = '/Users/macbook/RubymineProjects/proiect_sac/app/assets/python/venv/bin/python3 ' + python_cmd
    puts(python_cmd)
    escape_run python_cmd

    redirect_to recommend_path
  end

  def recommend
    @current_user = current_user
    file = File.open "public/uploads/" + current_user.id.to_s + "_files/output/testfile2.txt"
    text_data = file.read
    file.close

    score = UserScore.where(id_user: @current_user.id).first
    score.score = (text_data.to_i * 3 + score.score * 3)/4
    score.save

    @similar_essays = Essay.where(:score => (score.score)..(score.score + 10)).shuffle[0..4]
  end

  def read_essay
    @current_user = current_user
    @essay = Essay.where(:id => params[:id].to_i).first
    history = UserHistory.new
    history.id_user=@current_user.id
    history.id_essay=@essay.id
    history.save
    score = UserScore.where(id_user: @current_user.id).first
    score.score = (@essay.score + score.score * 3)/4
    score.save
  end

  private

  def escape_run param
    system param
  end
end
