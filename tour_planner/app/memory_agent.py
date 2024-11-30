from neo4j import GraphDatabase

class MemoryAgent:
    def __init__(self, uri="neo4j://localhost:7687", user="neo4j", password="password"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def store_preferences(self, user_id, preferences):
        with self.driver.session() as session:
            session.run("MERGE (u:User {id: $user_id}) "
                        "SET u.preferences = $preferences", user_id=user_id, preferences=preferences)

    def get_preferences(self, user_id):
        with self.driver.session() as session:
            result = session.run("MATCH (u:User {id: $user_id}) RETURN u.preferences", user_id=user_id)
            return result.single()[0]
