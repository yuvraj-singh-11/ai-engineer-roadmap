class LegalDocument:
    def __init__(self,document_id,title,document_type, content):
        if not document_id:
            raise ValueError("Document ID cannot be empty")
        if not title:
            raise ValueError("Document title cannot be empty")
        if not document_type:
            raise ValueError("Document type cannot be empty")
        if not content:
            raise ValueError("Document content cannot be empty")
        self.document_id = document_id
        self.title = title
        self.document_type = document_type
        self.content = content
        
            
        