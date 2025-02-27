from flask import Flask, request, jsonify
import os
import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

def find_files_by_fragment(directory, fragment):
    results = []
    directory = os.path.abspath(directory) 

    if not os.path.exists(directory) or not os.path.isdir(directory):
        logging.warning(f"Директория {directory} не существует или недоступна.")
        return []

    for root, _, files in os.walk(directory):
        for file in files:
            if fragment in file:
                file_path = os.path.join(root, file)
                try:
                    file_info = {
                        "name": file,
                        "path": file_path,
                        "size": os.path.getsize(file_path),
                        "created_at": datetime.datetime.fromtimestamp(os.path.getctime(file_path), datetime.UTC).isoformat()
                    }
                    results.append(file_info)
                except OSError as e:
                    logging.error(f"Ошибка при получении информации о файле {file_path}: {e}")
    
    return results

@app.route('/search', methods=['GET'])
def search_files():
    fragment = request.args.get('fragment', '').strip()
    directory = request.args.get('directory', os.getcwd()).strip()

    if not fragment:
        return jsonify({"error": "File fragment is required"}), 400

    logging.info(f"Поиск файлов с фрагментом '{fragment}' в директории '{directory}'")
    
    results = find_files_by_fragment(directory, fragment)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
