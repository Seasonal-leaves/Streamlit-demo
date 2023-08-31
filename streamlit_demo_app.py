import streamlit as st

def main():
  st.title("Finding largest among 3 numbers app")
  st.header("User input numbers")
  n1=st.number_input("Enter your 1st number :")
  n2=st.number_input("Enter your 2nd number :")
  n3=st.number_input("Enter your 3rd number :")
  if st.button("Which is the largest?"):
    max_num =  max(n1,n2,n3) 
    st.success(f"The largest number is : {max_num}") #What I have found out from my prior changes is that streamlit needs formatted print statements rather that multiple arguments
if __name__=="__main__":
  main()
    
