def cough_dec(func):

  def func_wrapper():
    # code before the function runs
    print('*cough*')
    func()
    # code after the function runs
    print('*cough*')

  return func_wrapper

@cough_dec
def question():
  print('Can you give me a discount on that?')

@cough_dec
def answer():
  print('It\'s only a dollar!')

question()
answer()