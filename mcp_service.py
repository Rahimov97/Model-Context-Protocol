from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)

def find_files_by_fragment(directory, fragment):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if fragment in file:
                file_path = os.path.join(root, file)
                file_info = {
                    "name": file,
                    "path": file_path,
                    "size": os.path.getsize(file_path),
                    "created_at": datetime.datetime.fromtimestamp(os.path.getctime(file_path)).isoformat()
                }
                results.append(file_info)
    return results

@app.route('/search', methods=['GET'])
def search_files():
    fragment = request.args.get('fragment', '')
    directory = request.args.get('directory', os.getcwd())
    
    if not fragment:
        return jsonify({"error": "File fragment is required"}), 400
    
    results = find_files_by_fragment(directory, fragment)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
