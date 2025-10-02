import streamlit as st
from google import genai
from PyPDF2 import PdfReader

client = genai.Client(api_key="AIzaSyCVR2c_azojOoqdSy4Jrb9CalE1Wqt3-lg")

st.title("PDF Summarizer with Gemini")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    numofpages = len(reader.pages)

    all_text = []

    for i in range(numofpages):
        page = reader.pages[i]
        text = page.extract_text()
        all_text.append(text)

    st.subheader("Extracted Text")

    subbject_section =f"""please extract the 'Property Address',
        'City',
        'County',
        'State',
        'Zip Code',
        'Borrower',
        'Owner of Public Record',
        'Legal Description',
        "Assessor's Parcel #",
        'Tax Year',
        'R.E. Taxes $',
        'Neighborhood Name',
        'Map Reference',
        'Census Tract',
        'Occupant',
        'Special Assessments $',
        'PUD',
        'HOA $ per year',
        'HOA $ per month',
        'Property Rights Appraised',
        'Assignment Type',
        'Lender/Client',
        'Address (Lender/Client)',
        'Offered for Sale in Last 12 Months',
        'Report data source(s) used, offering price(s), and date(s)' from {all_text}"""
    
    Neighborhood_section =f""" please extract the Neighborhood Section
          "Location",
          "Built-Up",
          "Growth",
          "Property Values",
          "Demand/Supply",
          "Marketing Time",
          "One-Unit",
          "2-4 Unit",
          "Multi-Family",
          "Commercial",
          "Other",
          "one unit housing price(high,low,pred)",
          "one unit housing age(high,low,pred)",
          "Neighborhood Boundaries",
          "Neighborhood Description",
          "Market Conditions:" from {all_text} but provide me exact values not suggestion text"""
    
    sales_grid =f""" please extract the sales comparision approach Section
          "Sale or Financing Concessions",
              "Date of Sale/Time",
              "Location",
              "Leasehold/Fee Simple",
              "Site",
              "View",
              "Design (Style)",
              "Quality of Construction",
              "Actual Age",
              "Condition",
              "Above Grade",
              "Room Count",
              "Gross Living Area",
              "Basement & Finished Rooms Below Grade",
              "Functional Utility",
              "Heating/Cooling",
              "Energy Efficient Items",
              "Garage/Carport",
              "Porch/Patio/Deck" from {all_text} but provide me exact values not suggestion text"""
    
    improvement_section =f""" please extract the improvement Section
          "Units", "# of Stories", "Type", "Existing/Proposed/Under Const.",
            "Design (Style)", "Year Built", "Effective Age (Yrs)", "Foundation Type",
            "Basement Area sq.ft.", "Basement Finish %", 
            "Evidence of Settlement",
            "Exterior Walls (Material/Condition)", "Roof Surface (Material/Condition)",
            "Gutters & Downspouts (Material/Condition)", "Window Type (Material/Condition)",
             "Storm Sash/Insulated", "Screens", "Floors (Material/Condition)", "Walls (Material/Condition)",
             "Trim/Finish (Material/Condition)", "Bath Floor (Material/Condition)", "Bath Wainscot (Material/Condition)",
             "Attic", "Heating Type", "Fuel", "Cooling Type",
             "Fireplace(s) #", "Patio/Deck", "Pool", "Woodstove(s) #", "Fence", "Porch", "Other Amenities",
             "Car Storage None", "Driveway # of Cars", "Driveway Surface", "Garage # of Cars", "Carport # of Cars",
             "Garage Att.", "Garage Det.", "Garage Built-in", "Appliances Refrigerator", "Appliances Range/Oven",
             "Appliances Dishwasher", "Appliances Disposal", "Appliances Microwave", "Appliances Washer/Dryer",
             "Appliances Other", "Finished area above grade Rooms", "Finished area above grade Bedrooms",
             "Finished area above grade Bath(s)", "Square Feet of Gross Living Area Above Grade",
             "Additional features", "Condition of the property",
             "Physical Deficiencies or Adverse Conditions",
             "Property Conforms to Neighborhood" from {all_text} but provide me exact values not suggestion text"""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=[subbject_section, Neighborhood_section, improvement_section, sales_grid]
    )

    st.subheader("Summarized Output")
    st.text(response.text.replace('**',''))