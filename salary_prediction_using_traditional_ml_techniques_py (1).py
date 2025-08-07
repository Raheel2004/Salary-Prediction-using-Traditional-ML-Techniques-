# Step 8: Streamlit App
# Save this section as app.py for deployment
"""
import streamlit as st
st.title("Salary Prediction App")

age = st.slider("Age", 20, 60)
experience = st.slider("Experience", 0, 40)
education = st.selectbox("Education Level", list(label_encoders['Education'].classes_))
skill = st.selectbox("Skill Level", list(label_encoders['Skill Level'].classes_))

# Convert input
input_df = pd.DataFrame({
    'Age': [age],
    'Experience': [experience],
    'Education': [label_encoders['Education'].transform([education])[0]],
    'Skill Level': [label_encoders['Skill Level'].transform([skill])[0]]
})

input_df[['Age', 'Experience']] = scaler.transform(input_df[['Age', 'Experience']])

prediction = rf.predict(input_df)[0]
st.success(f"Predicted Salary: ${prediction:,.2f}")
"""

# Step 9: Deployment
# Use 'render.yaml' or Render Dashboard to deploy the app
