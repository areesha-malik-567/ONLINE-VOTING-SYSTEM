class Candidate:
    def __init__(self, name):  
        self.name = name
        self.votes = 0

    def __str__(self):  
        return f"{self.name}: {self.votes} votes"


class Voter:
    def __init__(self, voter_id, name): 
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False

    def __str__(self):  
        return f"Voter ID: {self.voter_id}, Name: {self.name}, Voted: {self.has_voted}"


class OnlineVotingSystem:
    def __init__(self):  
        self.candidates = []
        self.voters = []
        self.votes = {}

    def add_candidate(self, name):
        candidate = Candidate(name)
        self.candidates.append(candidate)
        self.votes[name] = 0

    def add_voter(self, voter_id, name):
        voter = Voter(voter_id, name)
        self.voters.append(voter)

    def display_candidates(self):
        print("Candidates:")
        for candidate in self.candidates:
            print(candidate)

    def display_voters(self):
        print("Voters:")
        for voter in self.voters:
            print(voter)

    def vote(self, voter_id, candidate_name):
        voter = next((v for v in self.voters if v.voter_id == voter_id), None)
        if not voter:
            print("Voter not found.")
            return
        if voter.has_voted:
            print("You have already voted.")
            return

        candidate = next((c for c in self.candidates if c.name == candidate_name), None)
        if not candidate:
            print("Candidate not found.")
            return

        candidate.votes += 1
        self.votes[candidate_name] += 1
        voter.has_voted = True
        print(f"Thank you, {voter.name}. Your vote for {candidate_name} has been recorded.")

    def display_results(self):
        print("Voting Results:")
        for candidate, vote_count in self.votes.items():
            print(f"{candidate}: {vote_count} votes")



if __name__ == "__main__":
    voting_system = OnlineVotingSystem()

    
    voting_system.add_candidate("Ali Khan")
    voting_system.add_candidate("Fatima Ahmed")
    voting_system.add_candidate("Bilal Raza")

    
    voting_system.add_voter(1, "Usman Malik")
    voting_system.add_voter(2, "Ayesha Khan")
    voting_system.add_voter(3, "Zainab Ali")

    
    voting_system.display_candidates()
    voting_system.display_voters()

  
    voting_system.vote(1, "Ali Khan")
    voting_system.vote(2, "Fatima Ahmed")
    voting_system.vote(3, "Bilal Raza")
    voting_system.vote(1, "Fatima Ahmed")  

    
    voting_system.display_results()
