# A basic data base file to maintain integratity of the app


# Variables to store outputs from our model

user_prefrences = []
user_prefrences_uri = []
audio_features = []
similarity_matrix = []
recommendations = []

default_up = [
    "Bohemian Rhapsody",
    "Hotel California",
    "Imagine",
    "Like a Rolling Stone",
    "Purple Haze",
    "Stairway to Heaven",
    "Hey Jude",
    "Smells Like Teen Spirit",
    "Yesterday",
    "Let It Be",
    "Billie Jean",
    "Thriller",
    "Sweet Child o' Mine",
    "Wonderwall",
    "Wonderful Tonight",
    "Blackbird",
    "My Girl",
    "Hallelujah",
    "I Want to Hold Your Hand",
    "What's Going On"
]

# Default Display Text (About Section) 

about_txt = "Tune Fuse is a music Recommendation App, powered by advanced technology! It harness the remarkable power of cosine similarity and seamlessly integrated the Spotify API to bring you a personalized music discovery experience like never before. Say goodbye to the endless search for your next favorite track and let our app curate a tailored playlist that suits your unique tastes, making your music exploration a breeze. Discover the perfect harmony of math and music with our app today!"
cosine_sim_txt = "Cosine similarity is a metric for measuring how similar two vectors are. It's widely used in text analysis and recommendation systems. It calculates the cosine of the angle between the vectors, with 1 meaning identical, 0 for orthogonal (no similarity), and -1 for completely opposite. This metric is robust and efficient, making it valuable in various applications."
spoti_txt = "The Spotify API is a powerful tool that allows developers to integrate and interact with Spotify's music streaming platform in their own applications. It provides access to a wide range of music data, including track information, user playlists, and audio features. This API enables developers to create music-related applications, from playlist generators and music recommendations to music analysis tools. It has become a popular choice for building music-centric apps, enhancing user experiences, and creating innovative solutions within the world of music and entertainment."
