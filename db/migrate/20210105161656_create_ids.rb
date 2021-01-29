class CreateIds < ActiveRecord::Migration[5.2]
  def change
    create_table :ids do |t|
      t.string :user
      t.string :username
      t.string :password_digest
      t.string :name
      t.string :email

      t.timestamps
    end
  end
end
