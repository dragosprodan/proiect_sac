Rails.application.routes.draw do

  #register
  get 'register', to: 'home#register', as: 'register'
  post 'register', to: 'session#register'

  #login
  get 'login', to: 'home#login', as: 'login'
  post 'login', to: 'session#login'
  post 'logout', to: 'session#logout'

  #home
  get 'home', to: 'home#home', as: 'home'
  post 'uploads/:id', to: 'home#upload'
  delete 'delete', to: 'home#delete_upload'
  get 'recommend_score', to: 'home#recommend', as: 'recommend_score'

  #AI
  get 'edit_text', to: 'pymain#edit_text', as: 'edit_text'
  get 'recommend', to: 'pymain#recommend', as: 'recommend'

  #test
  get 'test', to: 'home#test_area', as: 'test'
  post 'run_stt', to: 'pymain#run_stt'
  post 'run_ta', to: 'pymain#run_ta'
  get 'read_essay/:id', to: 'pymain#read_essay', as: 'read_essay'

  # get 'import_data', to: 'home#import_data'
  root 'home#welcome'
end
