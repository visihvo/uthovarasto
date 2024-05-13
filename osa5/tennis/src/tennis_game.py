class TennisGame:
    SCORE_CALLS = ["Love", "Fifteen", "Thirty", "Forty"]
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        p1_score = self.m_score1
        p2_score = self.m_score2

        if p1_score == p2_score:
            return self._draw(p1_score)
        elif p1_score >= 4 or self.m_score2 >= 4:
            return self._check_adventage(p1_score, p2_score)
        else:
            return self._set_score(p1_score, p2_score)

    def _draw(self, score):
        if score < 3:
            return f"{self.SCORE_CALLS[score]}-All"
        else:
            return "Deuce"
        
    def _check_adventage(self, p1_score, p2_score):
        minus_result = p1_score - p2_score
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def _set_score(self, p1_score, p2_score):
        return f"{self.SCORE_CALLS[p1_score]}-{self.SCORE_CALLS[p2_score]}"