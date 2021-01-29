class User < ApplicationRecord
  has_secure_password

  has_one_attached :audio
end
