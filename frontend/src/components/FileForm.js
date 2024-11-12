import {useState} from 'react';

function FileForm() {
    const [file, setFile] = useState(null);

    const handleFileInputChange = (event) => {
        console.log(event.target);
        setFile(event.target.files[0]);
    }

    return (
        <div>
            <h1>Upload file</h1>
            <form>
                <div style={{marginBottom: "20px"}}>
                    <input type="file" onChange={handleFileInputChange} />
                </div>
                <button type="submit">Upload</button>
            </form>

            { file && <p>{file.name}</p> }
        </div>
    )
}

export default FileForm