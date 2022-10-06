from recordObserver import RecordObserver

# Observer Pattern - Subject
# subject class for adding observer and notify(update) usage
class Subject:
    observerList = []

    def addObserver(self, obs):
        self.observerList.append(obs)

    def notifyObserver(self, username, content):
        for obs in self.observerList:
            obs.update(username, content)