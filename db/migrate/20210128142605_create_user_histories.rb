class CreateUserHistories < ActiveRecord::Migration[5.2]
  def change
    create_table :user_histories do |t|
      t.integer :id_user
      t.integer :id_essay
      t.integer :essay_score

      t.timestamps
    end
  end
end
