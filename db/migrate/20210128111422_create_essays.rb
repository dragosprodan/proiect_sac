class CreateEssays < ActiveRecord::Migration[5.2]
  def change
    create_table :essays do |t|
      t.string :data
      t.integer :score

      t.timestamps
    end
  end
end
