class CreateUserScores < ActiveRecord::Migration[5.2]
  def change
    create_table :user_scores do |t|
      t.integer :id_user
      t.integer :score

      t.timestamps
    end
  end
end
