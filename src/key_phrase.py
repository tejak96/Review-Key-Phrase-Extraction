import warnings
import sys
sys.path.append("../tools/")
from read_data import get_data
from process_data import process_review, get_phrases
warnings.filterwarnings('ignore')

reviews=get_data()
for review in reviews:
    simplifiedTags=process_review(review)
    keyPhrases=get_phrases(simplifiedTags)
    print(review+' - '+', '.join(keyPhrases))


