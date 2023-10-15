import pandas as pd
#def change_categories(df):
def no_needed_columns(df):
    df.drop(['img', 'title', 'published_at', 'updated_at', 'workers'], axis=1, inplace=True)
    return df

def drop_duplicates(df):
    df = df.drop_duplicates(keep='first')
    return df
#-------------------------------------
def Transform_winner_column(df):
    df['winner'] = df['winner'].map({True: 1, False: 0})
    return df  

def drop_null_rows(df):
    df.drop([2261,2359,2454,2547,4525,4573], axis=0, inplace=True)
    return df 


# Spotify Transformation

def ms_to_min(df):
    df['duration_min'] = (df['duration_ms'] / 60000).round(2)  # Redondear a 2 decimales
    return df

def drop_unnamed_column(df): 
    df.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
    return df
#duplicados
def borrar_duplicados(df): 
    df.drop_duplicates(keep='first')
    return df
#borra el registro nulo
def borrar_nulos_spotify(df):
    df.drop([65900], axis=0, inplace=True)
    return df

#crea una nueva columna pasando los ms a minutos
def agregando_la_duracion_en_minutos(df):
    df['duration_min'] = (df['duration_ms'] / 60000).round(2)
    #df.head(2)
    return df

def categorizar_duracion(categorizar_duracion):
    if categorizar_duracion <= 3:
        return 'Poca_Duración'
    elif 3.0 < categorizar_duracion<= 4.0 :
        return 'Duración_Media'
    else:
        return 'Mucha_Duración'
    # Aplica la función para crear la nueva columna 'duration_category'
    
# Define una función que asigna la categoría según la popularidad
def categorizar_popularidad(popularidad):
    if popularidad <= 30:
        return 'Popularidad Baja'
    elif 30 < popularidad <= 60:
        return 'Popularidad Media'
    else:
        return 'Popularidad Alta'
    # Aplica la función para crear la nueva columna 'popularity_category'
    


#borrar guion
def crear_columnas_categoricas_(df):
    # Define los umbrales para las categorías
    umbrales_danceability = [0.0, 0.3, 0.7, 1.0]
    umbrales_energy = [0.0, 0.3, 0.7, 1.0]
    umbrales_valence = [0.0, 0.3, 0.7, 1.0]
    # Define los nombres de las categorías
    categorias = ['Baja', 'Media', 'Alta']
    categorias_valence = ['Negativa', 'Neutral', 'Positiva']

    # Utiliza pd.cut() para crear la nueva columna categórica
    df['danceability_category'] = pd.cut(df['danceability'], bins=umbrales_danceability, labels=categorias)
    df['energy_category'] = pd.cut(df['energy'], bins=umbrales_energy, labels=categorias)
    df['valence_category'] = pd.cut(df['valence'], bins=umbrales_valence, labels=categorias_valence)
    df['popularity_category'] = df['popularity'].apply(categorizar_popularidad)
    df['duration_categorys'] = df['duration_min'].apply(categorizar_duracion)
    return df

#group_by_categories_songs_of_grammys
def change_categories(df):
    categories = {
    'Soundtracks/Music Videos------': [
        'Best Song Written For Visual Media',
        'Best Compilation Soundtrack For Visual Media',
        'Best Score Soundtrack For Visual Media',
        'Best Music Video',
        'Best Music Film'
    ],
    'Production/Engineering------': [
        'Best Instrumental Arrangement',
        'Best Arrangement, Instrumental or A Cappella',
        'Best Arrangement, Instruments and Vocals',
        'Best Recording Package',
        'Best Boxed Or Special Limited Edition Package',
        'Best Album Notes',
        'Best Historical Album',
        'Best Engineered Album, Non-Classical',
        'Producer Of The Year, Non-Classical',
        'Best Remixed Recording',
        'Best Immersive Audio Album',
        'Best Engineered Album, Classical',
        'Producer Of The Year, Classical'
    ],
    'Pop------': [
        'Pop',
        'Best Traditional Pop Performance',
        'Best Pop Vocal Performance By A Duo, Group Or Chorus',
        'Best Pop Vocal Performance By A Duo Or Group',
        'Best Pop Vocal Collaboration',
        'Best Pop Performance By A Duo Or Group With Vocal',
        'Best Pop Collaboration With Vocals',
        'Best Pop Instrumental Performance',
        'Best Pop Vocal Collaboration',
        'Best Pop Vocal Performance By A Group',
        'Best Pop Vocal Performance By A Male',
        'Best Pop Vocal Performance By A Female',
        'Best Pop Performance By A Duo Or Group With Vocals',
        'Best Contemporary Single/Album',
        'Best Contemporary Female Solo Vocal Performance',
        'Best Contemporary Male Solo Vocal Performance',
        'Best Contemporary Vocal Performance By A Duo, Group Or Chorus',
        'Best Contemporary Instrumental Performance',
        'Best Contemporary Song',
        'Best Contemporary Album',
        'Best Contemporary Pop Vocal Performance, Female',
        'Best Contemporary Pop Vocal Performance, Male',
        'Best Contemporary Pop Performance - Vocal Duo Or Group',
        'Best Contemporary Pop Performance, Chorus',
        'Best Contemporary Pop Performance, Instrumental',
        'Best Performance By A "Top 40" Artist',
        'Best Pop Instrumental Performance By An Instrumental Performer',
        'Best Pop Instrumental Performance By An Arranger, Composer, Orchestra And/Or Choral Leader',
        'Best Contemporary Performance By A Chorus',
        'Best Pop Instrumental Performance (Orchestra, Group Or Soloist)',
        'Best Pop Instrumental Performance, (Orchestra, Group Or Soloist)',
        'Best Pop Vocal Performance By A Duo Or Group With Vocal',
        'Best Pop Vocal Collaboration'
    ],
    'Dance/Electronic------': [
        'Dance/Electronic',
        'Best Dance Recording',
        'Best Dance/Electronic Album',
        'Best Electronic/Dance Album',
        'Best Dance/Electronica Album'
    ],
    'Rock/Metal/Alternative------': [
        'Rock/Metal/Alternative',
        'Best Rock Instrumental Performance (Orchestra, Group Or Soloist)',
        'Best Hard Rock/Metal Performance Vocal Or Instrumental',
        'Rock',
        'Best Rock Performance',
        'Best Metal Performance',
        'Best Rock Song',
        'Best Rock Album',
        'Best Alternative Music Album',
        'Hard Rock Performance',
        'Best Hard Rock Performance',
        'Best Rock Vocal Performance',
        'Best Rock Performance By A Duo Or Group With Vocals',
        'Best Hard Rock Performance With Vocal',
        'Best Rock Vocal Performance, Solo',
        'Best Rock Vocal Performance, Female',
        'Best Rock Vocal Performance, Male',
        'Best Rock Vocal Performance, Male Or Female',
        'Best Male Rock Vocal Performance',
        'Best Female Rock Vocal Performance',
        'Best Rock Vocal Performance By A Duo Or Group',
        'Best Rock Performance - Duo Or Group',
        'Best Rock Instrumental Performance',
        'Best Rock Instrumental Performance - Group Or Soloist With Group',
        'Best Rock Gospel Album',
        'Best Traditional Gospel Album',
        'Best Contemporary R&B Gospel Album',
        'Best Rock Vocal Performance By A Duo Or Group',
        'Best Rock & Roll Recording',
        'Best New Artist Of 1964',
        'Best Rock & Roll Solo Vocal Performance - Male Or Female',
        'Best Rock & Roll Group Performance, Vocal Or Instrumental',
        'Best New Artist Of 1963',
        'Best Solo Vocal Performance, Female',
        'Best Solo Vocal Performance, Male',
        'Best Rock & Roll Recording',
        'Best Rock & Roll Solo Vocal Performance, Female',
        'Best Rock & Roll Solo Vocal Performance, Male',
        'Best Rock & Roll Group Performance, Vocal Or Instrumental',
        'Best New Artist Of 1962',
        'Best Instrumental Theme Or Instrumental Version Of Song',
        'Best Performance By A Dance Band',
        'Best Performance By A Vocal Group Or Chorus',
        'Best Rock & Roll Solo Vocal Performance, Male Or Female'
    ],
    'R&B/Urban------': [
        'R&B/Urban',
        'R&B/Soul',
        'Best R&B Performance',
        'Best Traditional R&B Performance',
        'Best R&B Song',
        'Best Urban Contemporary Album',
        'Best R&B Instrumental Performance (Orchestra, Group Or Soloist)',
        'Best R&B Album',
        'Best R&B/Sung Collaboration',
        'Best Female R&B Vocal Performance',
        'Best Male R&B Vocal Performance',
        'Best R&B Performance By A Duo Or Group With Vocals',
        'Best Traditional R&B Vocal Performance',
        'Best Urban/Alternative Performance',
        'Best Contemporary R&B Album',
        'Best Contemporary R&B Gospel Album',
        'Best R&B Instrumental Performance',
        'Best Traditional R&B Vocal Album',
        'Best R&B Vocal Performance By A Duo, Group Or Chorus',
        'Best Rhythm & Blues Vocal Performance, Female',
        'Best Rhythm & Blues Vocal Performance, Male',
        'Best Rhythm & Blues Solo Vocal Performance, Female',
        'Best Rhythm & Blues Solo Vocal Performance, Male',
        'Best Rhythm & Blues Group Performance, Vocal Or Instrumental',
        'Best Rhythm & Blues Solo Vocal Performance, Male Or Female',
        'Best Rhythm & Blues Recording',
        'Best Rhythm & Blues Performance By A Duo Or Group, Vocal Or Instrumental',
        'Best Rhythm & Blues Performance',
        'Best Rhythm & Blues Performance, Female',
        'Best Rhythm & Blues Performance, Male',
        'Best R&B Vocal Performance By A Duo Or Group',
        'Best R&B Vocal Performance By A Group',
        'Best Soul Gospel Performance',
        'Best Rhythm & Blues Vocal Performance, Female',
        'Best Rhythm & Blues Vocal Performance, Male',
        'Best Rhythm & Blues Performance By A Duo Or Group, Vocal Or Instrumental',
        'Best Rhythm & Blues Vocal Performance By A Group',
        'Best Rhythm & Blues Vocal Performance, Female',
        'Best Rhythm & Blues Vocal Performance, Male',
        'Best Rhythm & Blues Vocal Performance By A Duo Or Group',
        'Best Rhythm & Blues Vocal Performance By A Group',
        'Best Contemporary (R&R) Recording',
        'Best Contemporary (R&R) Solo Vocal Performance - Male Or Female',
        'Best Contemporary (R&R) Group Performance, Vocal Or Instrumental',
        'Best Contemporary (R&R) Single',
        'Best Contemporary (R&R) Vocal Performance - Female',
        'Best Contemporary (R&R) Vocal Performance - Male',
        'Best Contemporary (R&R) Performance - Group (Vocal Or Instrumental)',
        'Best Rhythm & Blues Solo Vocal Performance, Male Or Female'
    ],
    'Rap/Hip-Hop------': [
        'Rap/Hip-Hop',
        'Best Rap Performance',
        'Best Rap/Sung Performance',
        'Best Rap Song',
        'Best Rap Album',
        'Best Rap/Sung Collaboration',
        'Best Rap Solo Performance',
        'Best Rap Performance By A Duo Or Group',
        'Best Female Rap Solo Performance',
        'Best Male Rap Solo Performance'
    ],
    'Country------': [
        'Country',
        'Best Country Solo Performance',
        'Best Country Duo/Group Performance',
        'Best Country Song',
        'Best Country Album',
        'Best Country Vocal Performance',
        'Best Country Vocal Performance, Female',
        'Best Country Vocal Performance, Male',
        'Best Country Performance By A Duo Or Group With Vocals',
        'Best Country Collaboration With Vocals',
        'Best Country Instrumental Performance',
        'Best Country Instrumental Performance (Orchestra, Group Or Soloist)',
        'Best Country Vocal Performance, Duet',
        'Best New Country Song',
        'Best Country Performance Duo Or Group',
        'Best New Country Song',
        'Best Southern Gospel, Country Gospel Or Bluegrass Gospel Album',
        'Best Mexican-American/Tejano Music Performance',
        'Best Gospel/Contemporary Christian Music Performance',
        'Best Gospel Song',
        'Best Contemporary Christian Music Song',
        'Best Gospel Album',
        'Best Contemporary Christian Music Album',
        'Best Roots Gospel Album',
        'Best Latin Pop Album',
        'Best Latin Rock, Urban or Alternative Album',
        'Best Regional Mexican Music Album (Including Tejano)',
        'Best Tropical Latin Album',
        'Best Traditional Blues Album',
        'Best Contemporary Blues Album',
        'Best Folk Album',
        'Best Regional Roots Music Album',
        'Best Folk Recording'
    ],
    'Jazz/Blues------': [
        'Jazz/Blues',
        'Jazz',
        'Jazz (Continuación)',
        'Best Jazz Fusion Performance',
        'Best Jazz Instrumental Performance Soloist (On A Jazz Recording)',
        'Best Large Jazz Ensemble Performance',
        'Best Jazz Vocal Album',
        'Best Jazz Instrumental Album',
        'Best Jazz Instrumental Album, Individual or Group',
        'Best Jazz Performance By A Soloist',
        'Best Jazz Performance By A Group',
        'Best Jazz Performance By A Big Band',
        'Best Jazz Instrumental Performance - Group Or Soloist With Group',
        'Best Jazz Instrumental Performance - Soloist Or Small Group',
        'Best Jazz Performance, Individual',
        'Best Jazz Performance, Group',
        'Best Jazz Performance, Big Band',
        'Best Contemporary Jazz Album',
        'Best Jazz Composition Of More Than Five Minutes Duration',
        'Best Jazz Performance - Soloist Or Small Group (Instrumental)',
        'Best Jazz Performance - Large Group (Instrumental)',
        'Best Performance By An Orchestra - For Dancing',
        'Best Performance By An Orchestra Or Instrumentalist With Orchestra - Primarily Not Jazz Or For Dancing',
        'Best Jazz Vocal Performance, Duo Or Group',
        'Best Jazz Instrumental Performance, Soloist (On A Jazz Recording)'
    ],
    'Gospel/Christian------': [
        'Gospel/Christian',
        'Gospel/Christian (Continuación)',
        'Best Gospel Performance, Contemporary Or Inspirational',
        'Best Gospel Performance (Other Than Soul Gospel)',
        'Best Gospel Vocal Performance',
        'Best Gospel Vocal Performance, Female',
        'Best Gospel Vocal Performance, Male',
        'Best Gospel Vocal Performance By A Duo, Group, Choir Or Chorus',
        'Best Soul Gospel Vocal Performance, Male Or Female',
        'Best Soul Gospel Vocal Performance Duo, Group, Choir Or Chorus',
        'Best Southern, Country Or Bluegrass Gospel Album',
        'Best Gospel Or Other Religious Recording (Musical)',
        'Best Gospel Performance By A Choir Or Chorus',
        'Best Rock Or Rap Gospel Album',
        'Best Southern, Country, Or Bluegrass Gospel Album',
        'Best Gospel Album By A Choir Or Chorus',
        'Best Gospel Album',
        'Best Contemporary Christian Music Performance/Song',
        'Best Contemporary Christian Music Album',
        'Best Gospel/Contemporary Christian Music Performance',
        'Best Traditional Gospel Album',
        'Best Reggae Album',
        'Best Latin Rock, Urban or Alternative Album',
        'Best Tejano Album',
        'Best Norteño Album',
        'Best Banda Album',
        'Best Latin Urban Album',
        'Best Gospel Vocal Performance, Female',
        'Best Gospel Vocal Performance, Male',
        'Best Gospel Vocal Performance By A Duo, Group, Choir Or Chorus',
        'Best Soul Gospel Vocal Performance, Male Or Female',
        'Best Soul Gospel Vocal Performance Duo, Group, Choir Or Chorus',
        'Best Gospel Performance, Contemporary',
        'Best Gospel Performance, Traditional',
        'Best Gospel Performance By A Duo Or Group',
        'Best Soul Gospel Performance By A Duo Or Group',
        'Best Gospel Performance, Contemporary Or Inspirational'
    ],
    'Latin------': [
        'Latin',
        'Best Latin Jazz Album',
        'Best Latin Pop Album',
        'Best Regional Mexican Music Album (Including Tejano)',
        'Best Tropical Latin Album',
        'Best Mexican/Mexican-American Album',
        'Best Latin Rock, Alternative Or Urban Album',
        'Best Traditional Tropical Latin Album',
        'Best Salsa/Merengue Album',
        'Best Latin Rock/Alternative Album',
        'Best Latin Urban Album',
        'Best Latin Pop, Rock, Or Urban Album',
        'Best Regional Mexican Or Tejano Album',
        'Best Banda Or Norteño Album',
        'Best Small Ensemble Performance',
        'Best Latin Pop Performance',
        'Best Latin Rock/Alternative Performance',
        'Best Traditional Tropical Latin Performance',
        'Best Salsa Performance',
        'Best Merengue Performance',
        'Best Mexican-American Performance',
        'Best Tejano Performance',
        'Best Latin Performance',
        'Best Latin Pop Performance',
        'Best Latin Rock/Alternative Performance',
        'Best Latin Urban Performance',
        'Best Traditional Tropical Latin Performance',
        'Best Salsa Performance',
        'Best Merengue Performance',
        'Best Mexican-American Music Performance',
        'Best Tejano Music Performance',
        'Best Latin Pop Performance - Duo Or Group',
        'Best Latin Rock Or Alternative Performance',
        'Best Traditional Latin Tropical Performance',
        'Best Salsa Or Merengue Performance',
        'Best Mexican-American Or Tejano Music Performance',
        'Best Latin Jazz Performance',
        'Best Latin Pop Performance - Female',
        'Best Latin Pop Performance - Male',
        'Best Latin Rock/Alternative Performance - Duo Or Group',
        'Best Latin Rock/Alternative Performance - Female',
        'Best Latin Rock/Alternative Performance - Male',
        'Best Latin Urban Performance - Duo Or Group',
        'Best Latin Urban Performance - Female',
        'Best Latin Urban Performance - Male',
        'Best Traditional Tropical Latin Performance - Female',
        'Best Traditional Tropical Latin Performance - Male',
        'Best Salsa Performance - Duo Or Group',
        'Best Merengue Performance - Duo Or Group',
        'Best Mexican-American Performance - Duo Or Group',
        'Best Tejano Music Performance - Duo Or Group',
        'Best Latin Jazz Performance - Duo Or Group',
        'Best Latin Jazz Performance - Male',
        'Best Latin Jazz Performance - Female'
    ],
    'Reggae------': [
        'Reggae',
        'Best Reggae Album'
    ],
    'World Music------': [
        'World Music',
        'Best World Music Album',
        'Best Traditional World Music Album',
        'Best Contemporary World Music Album',
        'Best Musical Album For Children',
        'Best Spoken Word Album For Children',
        'Best Spoken Word Album (Includes Poetry, Audio Books & Story Telling)',
        'Best Song Written For Visual Media',
        'Best Song Written For A Motion Picture, Television Or Other Visual Media.'
    ],
    'Children\'s/Spoken Word/Comedy------': [
        'Children\'s/Spoken Word/Comedy',
        'Best Comedy Album',
        'Best Spoken Word Album (Includes Poetry, Audio Books & Storytelling)',
        'Best Spoken Word Album',
        'Best Spoken Comedy Album',
        'Best Spoken Word Album for Children',
        'Best Boxed Recording Package',
        'Best Album For Children',
        'Best Musical Show Album'
    ],
    'Other------': [
        'Other',
        'Miscellaneous',
        'Best Compilation Soundtrack Album For A Motion Picture, Television Or Other Visual Media',
        'Best Score Soundtrack Album For A Motion Picture, Television Or Other Visual Media',
        'Best Song Written For A Motion Picture, Television Or Other Visual Media',
        'Best Instrumental Arrangement Accompanying A Vocalist(s)',
        'Best Spoken Word Album (Includes Poetry, Audio Books & Storytelling)',
        'Best New Age Album',
        'Best Traditional Folk Album',
        'Best Contemporary Folk Album',
        'Best Hawaiian Music Album',
        'Best Native American Music Album',
        'Best Zydeco Or Cajun Music Album',
        'Best Traditional World Music Album',
        'Best Contemporary World Music Album',
        'Best Musical Show Album',
        'Best Compilation Soundtrack Album For Motion Picture, Television Or Other Visual Media',
        'Best Score Soundtrack Album For Motion Picture, Television Or Other Visual Media',
        'Best Song Written For Motion Picture, Television Or Other Visual Media',
        'Best Classical Album',
        'Best Instrumental Soloist(s) Performance (With Orchestra)',
        'Best Instrumental Soloist Performance (Without Orchestra)',
        'Best Chamber Music Performance',
        'Best Classical Vocal Performance',
        'Best Classical Contemporary Composition',
        'Best Classical Crossover Album',
        'Best Regional Mexican Album',
        'Best Latin Rock Or Alternative Album',
        'Best Latin Urban Album',
        'Best Contemporary Folk/Americana Album',
        'Best Polka Album',
        'Best Pop Performance By A Duo Or Group With Vocal',
        'Best Sound Track Album/Recording',
        'Best Original Score Written For A Motion Picture Or A Television Special',
        'Best Producer Of The Year',
        'Best Album Notes (Classical)',
        'Best Engineered Recording (Non-Classical)',
        'Best Engineered Recording (Classical)',
        'Best Album Cover (Other Than Classical)',
        'Best Sound Track Album/Recording'
    ],
    'Classical------': [
        'Classical',
        'Classical (Continuación)',
        'Best Classical Engineered Recording',
        'Classical Producer Of The Year',
        'Classical Producer Of The Year, Classical',
        'Best Choral Performance, Classical (Other Than Opera)',
        'Best Classical Performance - Instrumental Soloist Or Soloists (With Orchestra)',
        'Best Classical Performance - Instrumental Soloist OR Soloists (With Orchestra)',
        'Best Classical Performance- Instrumental Soloist Or Soloists (Without Orchestra)',
        'Best Classical Performance - Instrumentalist (With Concerto Scale Accompaniment)',
        'Best Classical Performance - Instrumentalist (Other Than Concerto-Scale Accompaniment)',
        'Best Classical Performance - Operatic Or Choral',
        'Best Classical Vocal Soloist Performance (With Or Without Orchestra)',
        'Best Classical Performance, Instrumental Soloist(s) (With Orchestra)',
        'Best Classical Performance, Instrumental Soloist(s) (Without Orchestra)',
        'Best Classical Performance - Chamber Music (Including Chamber Orchestra)',
        'Best Classical Performance - Concerto Or Instrumental Soloist (With Full Orchestral Accompaniment)',
        'Best Choral Performance (Other Than Opera)',
        'Best Classical Performance, Instrumental Soloist (With Orchestra)',
        'Best Classical Performance, Instrumental Soloist (Without Orchestra)',
        'Best Chamber Music Or Other Small Ensemble Performance',
        'Best Engineered Recording - Classical',
        'Best Orchestral Recording',
        'Best Classical Performance - Instrumental Soloist(s) (With Orchestra)',
        'Best Classical Performance - Instrumental Soloist(s) (Without Orchestra)',
        'Best Classical Orchestral Recording',
        'Best Album Notes, Classical',
        'Best New Classical Artist',
        'Best New Classical Composition',
        'Best Classical Performance - Concerto Or Instrumental Soloist (Other Than Full Orchestral Accompaniment)',
        'Best Classical Performance - Vocal Soloist',
        'Best Classical Opera Production',
        'Album Of The Year - Classical',
        'Album Of The Year, Classical',
        'Album Of Best Original Score Written For A Motion Picture Or Television Special',
        'Best Classical Chamber Music Performance - Instrumental Or Vocal',
        'Best Classical Performance, Orchestra',
        'Best Composition By A Contemporary Classical Composer',
        'Most Promising New Classical Recording Artist',
        'Best Album Notes, Classical',
        'Best Album Cover, Photography',
        'Best Album Cover, Graphic Arts',
        'Best Album Cover - Other Than Classical',
        'Best Album Cover - Classical',
        'Best Engineering Contribution - Classical Recording',
        'Best Engineered Record (Classical)',
        'Best Engineered Recording - Classical',
        'Best Engineered Recording - Other Than Classical Or Novelty'
    ],
    'Production/Engineering------': [
        'Production/Engineering',
        'Best Engineered Album - Non-Classical',
        'Producer Of The Year',
        'Producer Of The Year, Non-Classical',
        'Best Engineered Recording - Special Or Novel Effects',
        'Best Engineering Contribution - Other Than Classical Or Novelty',
        'Best Engineering Contribution - Novelty Recording',
        'Best Engineering Contribution',
        'Best Engineering Contribution - Popular Recording',
        'Best Engineering Contribution - Other Than Classical Or Novelty'
    ],
    'Children\'s Album------': [
        'Children\'s Album',
        'Best Album For Children',
        'Best Children\'s Music Album',
        'Best Recording For Children',
        'Best Musical Cast Show Album'
    ],
    'Surround Sound Album------': [
        'Surround Sound Album',
        'Best Surround Sound Album'
    ],
    'Soundtracks/Music Videos------': [
        'Soundtracks/Music Videos',
        'Best Compilation Soundtrack Album For Visual Media',
        'Best Score Soundtrack Album For Visual Media',
        'Best Music Video',
        'Best Music Film'
    ],
    'Folk/World Music------': [
        'Folk/World Music',
        'Best Folk Recording',
        'Best Traditional Pop Vocal Performance',
        'Best Traditional Pop Vocal Performance, Male Or Female',
        'Best Traditional Pop Vocal Performance - Male',
        'Best Traditional Pop Vocal Performance - Female',
        'Best Pop Vocal Collaboration',
        'Best Country Vocal Collaboration',
        'Best Latin Pop Performance - Duo Or Group',
        'Best Pop Performance By A Duo Or Group With Vocals',
        'Best Pop Collaboration With Vocals',
        'Best Pop Instrumental Performance',
        'Best Pop Vocal Collaboration',
        'Best Contemporary Single/Album'
    ],
    'Spoken Word Album/Documentary/Drama------': [
        'Spoken Word Album',
        'Best Spoken Word Album',
        'Best Spoken Word Or Drama Recording',
        'Best Spoken Word Album (Includes Poetry, Audio Books & Storytelling)',
        'Best Comedy Recording',
        'Best Comedy Performance',
        'Best Comedy Album',
        'Best Comedy Album',
        'Best Comedy Album',
        'Best Spoken Word Album for Children',
        'Best Spoken Word Or Non-Musical Album',
        'Best Spoken Word Or Non-Musical Recording',
        'Best Comedy Recording',
        'Best Spoken Word Or Drama Recording',
        'Best Comedy Album',
        'Best Spoken Word, Documentary Or Drama',
        'Best Spoken Word Recording',
        'Best Spoken Word Album',
        'Best Spoken Word Or Drama Recording',
        'Best Spoken Comedy Album',
        'Best Spoken Word Album for Children',
        'Best Spoken Word Or Non-Musical Album',
        'Best Documentary, Spoken Word Or Drama Recording (Other Than Comedy)',
        'Best Comedy Performance',
        'Best Comedy Album',
        'Best Comedy Performance - Spoken Word'
    ],
    'Song Written For Visual Media------': [
        'Song Written For Visual Media',
        'Best Song Written For Visual Media',
        'Best Song Written For A Motion Picture, Television Or Other Visual Media.',
        'Best Song Written Specifically For A Motion Picture Or For Television',
        'Best Song Written For A Motion Picture, Television Or Other Visual Media.',
        'Best Song Written For A Motion Picture Or For Television',
        'Best Rhythm & Blues Song',
        'Best Original Score Written For A Motion Picture Or A Television Show',
        'Best Original Score Written For A Motion Picture Or A Television Special',
        'Best Original Score From A Motion Picture Or Television Show',
        'Best Composition By A Contemporary Composer',
        'Best Contemporary Composition'
    ],
    'Instrumental Soloist Performance------': [
        'Instrumental Soloist Performance',
        'Best Instrumental Composition',
        'Best Instrumental Composition Written For A Motion Picture, Television Or Other Visual Media.',
        'Best Instrumental Soloist(s) Performance (With Orchestra)',
        'Best Instrumental Soloist Performance (Without Orchestra)',
        'Best Instrumental Performance',
        'Best Classical Choral Performance',
        'Best Instrumental Arrangement',
        'Best Instrumental Arrangement With Accompanying Vocal(s)',
        'Best Arrangement Accompanying Vocals/Instrumentals',
        'Best Instrumental Arrangement Accompanying A Vocalist(s)',
        'Best Instrumental Arrangement Accompanying Vocal(s)'
    ],
    'Southern/Country/Bluegrass Gospel------': [
        'Southern/Country/Bluegrass Gospel',
        'Best Southern, Country, Or Bluegrass Gospel Album',
        'Best Traditional Soul Gospel Album',
        'Best Contemporary Soul Gospel Album',
        'Best Gospel Choir Or Chorus Album',
        'Best Gospel Album By A Choir Or Chorus'
    ],
    'Mexican-American/Tejano Music------': [
        'Mexican-American/Tejano Music',
        'Best Mexican-American Music Performance',
        'Best Tejano Music Performance',
        'Best Mexican-American Album'
    ],
    'Étnico y Tradicional------': [
        'Best Ethnic Or Traditional Recording',
        'Best Ethnic Or Traditional Folk Recording',
        'Best Latin Recording',
        'Best Ethnic Or Traditional Recording (Including Traditional Blues)',
        'Best Traditional Soul Gospel Performance',
        'Best Traditional Blues Recording',
        'Best Contemporary Blues Recording',
        'Best Traditional Folk Recording',
        'Best Polka Recording',
        'Best Gospel Performance, Female',
        'Best Gospel Performance, Male',
        'Best Gospel Performance Contemporary Or Inspirational',
        'Best Southern Gospel Album',
        'Best Album Package',
        'Best Album Cover - Photography',
        'Best Album Cover - Graphic Arts',
        'Best Album Cover - Boxed',
        'Best Album Or Original Instrumental Background Score Written For A Motion Picture Or Television',
        'Best Album Of Original Score Written For A Motion Picture Or A Television Special',
        'Best Album Of Original Instrumental Background Score Written For A Motion Picture Or Television',
        'Música de Escena y Musicales'
    ],
    'Video y Multimedia------': [
        'Best Performance Music Video',
        'Best Concept Music Video',
        'Best Video, Short Form',
        'Best Video Album'
    ],
    'Otras Categorías Relacionadas------': [
        'Producer Of The Year, (Non-Classical)',
        'Best New Age Recording',
        'Best Inspirational Performance',
        'Best New Artist Of 1963',
        'Best Album Cover - Other Than Classical'
    ],
    'Música de Escena y Musicales ------': [
        'Best Musical Cast Show Album',
        'Best Album Of Original Instrumental Background Score Written For A Motion Picture Or Television Special',
        'Best Song Written Specifically For A Motion Picture Or Television',
        'Best Album Of Original Score Written For A Motion Picture Or Television Special',
        'Best Original Score Written For A Motion Picture Or A Television Special',
        'Best Sound Track Album Or Recording Of Music Score From Motion Picture Or Television'
    ],
    'Arrangement Categories--------': [
        'Best Arrangement, Instrumental or A Cappella',
        'Best Arrangement, Instruments and Vocals',
        'Best Arrangement On An Instrumental',
        'Best Arrangement On An Instrumental Recording',
        'Best Arrangement Accompanying Vocalist(s)',
        'Best Arrangement For Voices',
        'Best Arrangement Accompanying Vocal(s)',
        'Best Arrangement Accompanying Vocals',
        'Best Arrangement For Voices (Duo, Group Or Chorus)',
        'Best Arrangement Accompanying Vocalists',
        'Best Accompaniment Arrangement For Vocalist(s) Or Instrumentalist(s)',
        'Best Background Arrangement (Behind vocalist or instrumentalist)'
    ],
    'Main Recording Categories---------:': [
        'Record Of The Year',
        'Album Of The Year',
        'Song Of The Year',
        'Best New Artist',
        'Best American Roots Performance',
        'Best American Roots Song',
        'Best Americana Album',
        'Best Bluegrass Album',
        'Best Musical Theater Album',
        'Best Compilation Soundtrack For Visual Media',
        'Best Score Soundtrack For Visual Media',
        'Best Immersive Audio Album',
        'Best Orchestral Performance',
        'Best Opera Recording',
        'Best Choral Performance',
        'Best Chamber Music/Small Ensemble Performance',
        'Best Blues Album',
        'Best Gospel Performance',
        'Best Alternative Music Performance',
        'Best Soundtrack Album',
        'Best Recording Package',
        'Best Boxed Or Special Limited Edition Package',
        'Best Album Notes',
        'Best Historical Album',
        'Best Remixed Recording'
    ],}
    def etiquetar_categoria(category):
        for clave, palabras_clave in categories.items():
            for palabra_clave in palabras_clave:
                if palabra_clave in category:
                    return clave
        return category
    df['category'] = df['category'].apply(etiquetar_categoria)
    return df