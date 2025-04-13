import json
import time

class MockHyperledgerClient:
    """Mock Hyperledger client for demo purposes"""
    
    def __init__(self):
        self.documents = {}
    
    def add_document(self, doc_hash, metadata):
        """Add document to mock Hyperledger ledger"""
        self.documents[doc_hash] = {
            "exists": True,
            "timestamp": int(time.time()),
            "metadata": metadata
        }
        return {"status": "SUCCESS", "txid": "hyperledger_tx_" + doc_hash[:8]}
    
    def verify_document(self, doc_hash):
        """Verify document in mock Hyperledger ledger"""
        if doc_hash in self.documents:
            return {
                "verified": True,
                "data": self.documents[doc_hash]
            }
        return {"verified": False, "data": {}}

# Singleton instance for demo
hyperledger_client = MockHyperledgerClient()

def add_document_to_hyperledger(doc_hash, metadata):
    """Add document hash to Hyperledger Fabric"""
    try:
        result = hyperledger_client.add_document(doc_hash, metadata)
        return {
            "status": "success",
            "tx_id": result["txid"]
        }
    except Exception as e:
        print(f"Error adding document to Hyperledger: {e}")
        return {"status": "error", "message": str(e)}

def verify_document_on_hyperledger(doc_hash):
    """Verify document hash on Hyperledger Fabric"""
    try:
        result = hyperledger_client.verify_document(doc_hash)
        return result
    except Exception as e:
        print(f"Error verifying document on Hyperledger: {e}")
        return {"verified": False, "message": str(e)}