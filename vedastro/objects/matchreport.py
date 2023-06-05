import VedAstro.Library as libray

from vedastro.objects import Person


#        public MatchReport(string id, Person male, Person female, double kutaScore, string notes, List<MatchPrediction> prediction_list, string[] user_id)
class MatchReport(libray.MatchReport):
    def __init__(self, id:str, male:Person, female:Person, kuta_score:float, notes:str, prediction_list:[MatchPrediction], user_id:[str]):
        super().__init__(id, male, female, kuta_score, notes, prediction_list, user_id)
