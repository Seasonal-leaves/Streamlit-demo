import streamlit as st
'''def find_largest(num1,num2,num3):
  return max(num1,num2,num3)'''
def main():
  st.write("
  Finding largest among 3 numbers app
  ")
  st.header("User input numbers")
  n1=st.number_input("Enter your 1st number :")
  n2=st.number_input("Enter your 2nd number :")
  n3=st.number_input("Enter your 3rd number :")
  if st.button("Which is the largest?"):
    #largest = find_largest(n1,n2,n3)
    max_num =  max(n1,n2,n3)
    st.success(f"The largest number is : {max_num}")
if __name__=="__main__":
  main()
    
