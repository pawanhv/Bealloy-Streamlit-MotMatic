Alloyimport openai
import streamlit as st



# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="MotMatic par Bealloy", page_icon="img/rephraise_logo.png",)


# Design change spinner color to primary color
st.markdown('''<style>.stSpinner > div > div {border-top-color: #9d03fc;}</style>''',
    unsafe_allow_html=True)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        footer {
	
                        	visibility: hidden;
                        	
                        	}
                        </style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

# Connect to OpenAI GPT-3, fetch API key from Streamlit secrets
openai.api_key = st.secrets["API"]

def gen_mail_contents(email_contents):

    # iterate through all seperate topics
    for topic in range(len(email_contents)):
        input_text = email_contents[topic]
        rephrased_content = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f'''Please edit the following French text for grammar, structure, and spelling errors, so that it reads as if it were written by a native speaker. Your edited text should be well-organized, coherent, and free of any mistakes that would detract from the writer's intended meaning. Please also ensure that the text uses appropriate vocabulary and phrasing, and that any idiomatic expressions are translated accurately.
                    Please note that you should also strive to maintain the tone and style of the original text while correcting errors and improving clarity.
                    Je suis allé à l'école hier.: Je suis allé(e) à l'école hier.
                    Il parle lentement.: Il parle lentement.
                    Elle ne parle pas français pas.: Elle ne parle pas français.
                    Je suis étudiant dans l'université.: Je suis étudiant(e) à l'université.
                    Je vais à l'école par le bus.: Je vais à l'école en bus.
                    Je suis allé(e) à le cinéma hier soir.: Je suis allé(e) au cinéma hier soir.
                    Je ne veux pas rien faire.: Je ne veux rien faire.
                    Je vais à la plage pendant l'été.: Je vais à la plage en été.
                    Je n'ai pas vu personne.: Je n'ai vu personne.
                    Je n'ai pas le temps pour faire du sport.: Je n'ai pas le temps de faire du sport.
                    Je ne sais pas rien.: Je ne sais rien.
                    Il a mangé vite.: Il a mangé rapidement.
                    Elle court rapide.: Elle court rapidement.
                    Il fait froides aujourd'hui.: Il fait froid aujourd'hui.
                    J'ai reçu un cadeau sucré.: J'ai reçu un cadeau sucré.
                    Je vais à le cinéma: Je vais au cinéma.
                    J'ai eu un bon note à l'examen.: J'ai eu une bonne note à l'examen.
                    Il chante mauvais.: Il chante mal.
                    Il faut faire attention aux voitures.: Il faut faire attention aux voitures.
                    Il a mangé une salade délicieuse.: Il a mangé une salade délicieuse.
                    Je préfère étudier le mathématiques.: Je préfère étudier les mathématiques.
                    Elle a acheté de nouveaux vêtements.: Elle a acheté de nouveaux vêtements.
                    J'ai mangé une pizza amère.: J'ai mangé une pizza épicée.
                    J'ai mangé trop de chocolat.: J'ai mangé trop de chocolats.
                    Elle travaille dur.: Elle travaille dur.
                    Je vais à l'école par le bus.: Je vais à l'école en bus.
                    Je suis tombé(e) sur l'amour avec la première vue.: Je suis tombé(e) amoureux/amoureuse au premier regard.
                    Je suis alé(e) au cinéma hier.: Je suis allé(e) au cinéma hier.
                    Je suis alé(e) au parc pour la dimanche.: Je suis allé(e) au parc dimanche.
                    Elle a les yeux verts foncés.: Elle a les yeux d'un vert foncé.
                    On se voit demain soir.: On se voit demain soir.
                    Nous avons pris des photots.: Nous avons pris des photos.
                    Elle travaille dans le bureau.: Elle travaille au bureau.
                    Elle a acheté un chapeau baut.: Elle a acheté un chapeau beau.
                    J'aime écouter la musiques.: J'aime écouter la musique.
                    J'ai étudie beaucoup pour l'examen.: J'ai beaucoup étudié pour l'examen.
                    J'ai mangé le dîner avec le restaurant.: J'ai mangé le dîner au restaurant.
                    Je ne comprends pas rien.: Je ne comprends rien.
                    Nous avons pris des photots.: Nous avons pris des photos.
                    Elle a mangé un bon repas.: Elle a mangé un bon repas.
                    {input_text}.:''',
                    # prompt=f"Rewrite the text to sound professional, elaborate and polite.\nText: {input_text}\nRewritten text:",
                    temperature=0.8,
                    max_tokens=len(input_text)*3,
                    top_p=0.8,
                    best_of=2,
                    frequency_penalty=0.0,
                    presence_penalty=0.0)

        # replace existing topic text with updated
        email_contents[topic] = rephrased_content.get("choices")[0]['text']
    return email_contents

def main_gpt3emailgen():
    st.header("MotMatic : Votre outil secret pour une communication écrite impeccable")
    st.write("Découvrez MotMatic, l'outil ultime pour améliorer votre écriture. Développé par [BeAlloy](https://be-alloy.com), il vous aide à communiquer de manière claire et professionnelle. [Essayez notre démo gratuite dès maintenant !](https://app.be-alloy.com/register)")
    st.image('img/momatic_banner.png')  # TITLE and Creator information
    st.write("\n")
    st.subheader('\nExprimez-vous librement et laissez la magie opérer ! \n')
    with st.container():

        input_c1 = st.text_area('Saisissez le contenu de votre e-mail ci-dessous :', '',height=350, max_chars=2000)

        email_text = ""  # initialize columns variables
        
        st.write("\n")  # add spacing
        st.write("\n")  # add spacing
        if (True):
            columns = st.columns((2, 1, 2))
            
            if columns[1].button('Corriger'):
                with st.spinner(text="En cours..."):

                    input_contents = []  # let the user input all the data
                    if (input_c1 != "") and (input_c1 != 'topic 1'):
                        input_contents.append(str(input_c1))

                    if (len(input_contents) == 0):  # remind user to provide data
                        st.write('Veuillez remplir le contenu de votre message!')
                    
                    if (len(input_contents) >= 1):  # initiate gpt3 mail gen process
                        email_text = gen_mail_contents(input_contents)
    if email_text != "":
        st.write('\n')  # add spacing
        st.subheader('\nVotre texte corrigé se trouve ci-dessous!\n')
        with st.container():
            st.text_area('',email_text[0],height=350, max_chars=2000)  #output the results


if __name__ == '__main__':
    # call main function
    main_gpt3emailgen()
