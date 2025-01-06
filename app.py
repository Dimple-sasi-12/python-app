from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Expanded list of symptoms (from birth to death) with their respective recommendations
symptoms_list = [
    'fever', 'headache', 'cold', 'stomach pain', 'diarrhea', 'fatigue', 'vomiting', 'cough',
    'chest pain', 'dizziness', 'sore throat', 'muscle pain', 'joint pain', 'rash', 'swelling',
    'skin irritation', 'ear pain', 'toothache', 'constipation', 'nausea', 'severe weakness', 
    'blood in stool', 'runny nose', 'sore eyes', 'abdominal pain', 'sore gums', 'hives', 'sinus infection',
    'croup', 'chickenpox', 'diabetic complications', 'stroke', 'heart attack', 'feeling faint', 'high blood pressure'
]

# Expanded medicine recommendations based on symptoms and age
recommendations = {
    'fever': 'Take Paracetamol (500mg) for fever. Consult a doctor for high fever.',
    'headache': 'Take Ibuprofen (200mg) for headache. Rest in a quiet place.',
    'cold': 'Take Cough Syrup (10ml) for cold. Drink warm fluids.',
    'stomach pain': 'Take Antacid or consult a doctor if pain persists.',
    'diarrhea': 'Take ORS (Oral Rehydration Solution) to stay hydrated. Consult a doctor if symptoms persist.',
    'fatigue': 'Take Rest and drink plenty of fluids.',
    'vomiting': 'Take antiemetic medicine like Ondansetron (4mg). Consult a doctor if persistent.',
    'cough': 'Take Cough Syrup (10ml) or consult a doctor if severe.',
    'chest pain': 'Consult a doctor immediately, as chest pain can indicate serious conditions.',
    'dizziness': 'Take Rest and hydrate, consult a doctor if dizziness persists.',
    'sore throat': 'Take throat lozenges or Gargle with warm salt water.',
    'muscle pain': 'Take Ibuprofen (200mg) or consult a doctor if pain persists.',
    'joint pain': 'Take Ibuprofen (200mg) or consult a doctor if pain persists.',
    'rash': 'Consult a doctor for treatment depending on the rash type.',
    'swelling': 'Apply Ice or consult a doctor if swelling persists.',
    'skin irritation': 'Apply hydrocortisone cream or consult a doctor for severe irritation.',
    'ear pain': 'Consult a doctor for ear infections, take pain relievers for temporary relief.',
    'toothache': 'Take Ibuprofen (200mg) or consult a dentist.',
    'constipation': 'Increase fiber intake, drink plenty of water. Take laxatives if needed.',
    'nausea': 'Take antiemetic medication like Ondansetron, and hydrate.',
    'severe weakness': 'Consult a doctor as this could indicate underlying conditions.',
    'blood in stool': 'Consult a doctor immediately for a proper diagnosis.',
    'runny nose': 'Use nasal decongestant or saline spray, hydrate, and rest.',
    'sore eyes': 'Use eye drops, consult a doctor for any underlying issues.',
    'abdominal pain': 'Consult a doctor for proper diagnosis, take antacids for mild pain.',
    'sore gums': 'Use antiseptic mouthwash or consult a dentist for gum infection.',
    'hives': 'Take antihistamine for itching, consult a doctor if symptoms persist.',
    'sinus infection': 'Take a decongestant, consult a doctor for antibiotics if needed.',
    'croup': 'Consult a doctor immediately for treatment of this respiratory condition.',
    'chickenpox': 'Consult a doctor for antiviral treatment, take antihistamine for itching.',
    'diabetic complications': 'Monitor blood sugar levels and consult a doctor for advice.',
    'stroke': 'Consult a doctor immediately. Time is crucial during a stroke.',
    'heart attack': 'Call emergency services immediately. Aspirin may be recommended before medical help arrives.',
    'feeling faint': 'Sit down and rest. Drink water, consult a doctor if symptoms persist.',
    'high blood pressure': 'Consult a doctor for treatment, monitor blood pressure regularly.'
}

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html', symptoms=symptoms_list)

# Route to process form submissions
@app.route('/', methods=['POST'])
def recommend_medicine():
    symptom = request.form.get('symptom').lower()
    age = request.form.get('age')
    
    # If the symptom is in the recommendations dictionary, suggest the medicine
    recommendation = recommendations.get(symptom, 'Consult a doctor for further advice.')
    
    corrected_symptom = symptom.capitalize()  # Ensure the first letter is capitalized
    return render_template('index.html', symptoms=symptoms_list, recommendation=recommendation, corrected_symptom=corrected_symptom)

# Route to get dynamic suggestions for symptoms
@app.route('/get_symptom_suggestions', methods=['GET'])
def get_symptom_suggestions():
    query = request.args.get('query', '')
    matched_symptoms = [symptom for symptom in symptoms_list if symptom.lower().startswith(query.lower())]
    return jsonify(matched_symptoms)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Ensure the app listens on all interfaces for mobile access
