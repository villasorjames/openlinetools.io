from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

CUSTOM_LICENSE_PRIVATE_KEY = "9DBC845E9018537810FDAE62824322EEE1B12BAD81FCA28EC295FB397C61CE0B"

def generate_license(software_id, license_type):
    try:
        # Fixed license level - you can change this value as needed
        LICENSE_LEVEL = 6  # Change this to your desired fixed level
        
        if license_type == 'ros':
            cmd = ['python', 'license.py', 'licgenros', software_id, CUSTOM_LICENSE_PRIVATE_KEY]
        else:  # chr
            cmd = ['python', 'license.py', 'licgenchr', software_id, CUSTOM_LICENSE_PRIVATE_KEY]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>MikroTik License Generator</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * { 
                box-sizing: border-box; 
                margin: 0; 
                padding: 0; 
            }
            
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                line-height: 1.6;
            }
            
            .container { 
                max-width: 100%;
                margin: 0 auto; 
                background: white; 
                padding: 25px 20px;
                border-radius: 20px; 
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            }
            
            @media (min-width: 768px) {
                .container {
                    max-width: 500px;
                    padding: 30px;
                }
            }
            
            h1 { 
                text-align: center; 
                color: #2c3e50; 
                margin-bottom: 25px;
                font-size: 1.5rem;
                font-weight: 700;
            }
            
            .info-banner {
                background: linear-gradient(135deg, #e3f2fd, #bbdefb);
                border-left: 4px solid #2196f3;
                padding: 15px;
                margin-bottom: 25px;
                border-radius: 8px;
                font-size: 0.9rem;
                color: #1565c0;
            }
            
            .form-group { 
                margin-bottom: 25px; 
            }
            
            label { 
                display: block; 
                margin-bottom: 8px; 
                font-weight: 600;
                color: #2c3e50;
                font-size: 0.95rem;
            }
            
            input, select { 
                width: 100%; 
                padding: 16px 18px; 
                border: 2px solid #e1e8ed; 
                border-radius: 12px; 
                font-size: 1rem;
                background: #fafbfc;
                transition: all 0.3s ease;
                -webkit-appearance: none;
                appearance: none;
            }
            
            input:focus, select:focus {
                border-color: #3498db;
                outline: none;
                background: white;
                box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
                transform: translateY(-2px);
            }
            
            .generate-btn {
                background: linear-gradient(135deg, #3498db, #2980b9);
                color: white;
                padding: 18px;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                font-size: 1.1rem;
                font-weight: 700;
                width: 100%;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
                margin-top: 10px;
            }
            
            .generate-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(52, 152, 219, 0.4);
            }
            
            .generate-btn:active {
                transform: translateY(-1px);
            }
            
            .generate-btn:disabled {
                opacity: 0.7;
                transform: none;
                box-shadow: none;
                cursor: not-allowed;
            }
            
            .license-container { 
                background: #f8f9fa; 
                padding: 25px; 
                margin-top: 25px; 
                border-radius: 15px; 
                border-left: 5px solid #27ae60;
                display: none;
                position: relative;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            }
            
            .copy-btn {
                position: absolute;
                top: 15px;
                right: 15px;
                background: linear-gradient(135deg, #27ae60, #219a52);
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 0.9rem;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 2px 10px rgba(39, 174, 96, 0.3);
            }
            
            .copy-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 15px rgba(39, 174, 96, 0.4);
            }
            
            .copy-btn.copied {
                background: linear-gradient(135deg, #3498db, #2980b9);
                transform: scale(0.95);
            }
            
            .license-text {
                white-space: pre-wrap; 
                font-family: 'Courier New', monospace;
                font-size: 0.9rem;
                line-height: 1.5;
                color: #2c3e50;
                margin-right: 80px;
                overflow-wrap: break-word;
            }
            
            .loading {
                text-align: center;
                padding: 20px;
                color: #666;
                font-size: 1rem;
                display: none;
            }
            
            .loading-spinner {
                border: 3px solid #f3f3f3;
                border-top: 3px solid #3498db;
                border-radius: 50%;
                width: 30px;
                height: 30px;
                animation: spin 1s linear infinite;
                margin: 0 auto 15px;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            /* Mobile optimizations */
            @media (max-width: 480px) {
                body {
                    padding: 15px;
                }
                
                .container {
                    padding: 20px 15px;
                    border-radius: 15px;
                }
                
                h1 {
                    font-size: 1.3rem;
                    margin-bottom: 20px;
                }
                
                input, select {
                    padding: 14px 16px;
                    font-size: 16px; /* Prevents zoom on iOS */
                }
                
                .generate-btn {
                    padding: 16px;
                    font-size: 1rem;
                }
                
                .license-container {
                    padding: 20px;
                }
                
                .copy-btn {
                    padding: 10px 16px;
                    font-size: 0.85rem;
                    top: 12px;
                    right: 12px;
                }
                
                .license-text {
                    font-size: 0.85rem;
                    margin-right: 70px;
                }
            }
            
            /* Touch device optimizations */
            @media (hover: none) {
                .generate-btn:hover,
                .copy-btn:hover {
                    transform: none;
                }
                
                .generate-btn:active,
                .copy-btn:active {
                    transform: scale(0.98);
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>MikroTik v7.17 License Generator</h1>
            
            <div class="info-banner">
                <strong>License Level:</strong> All generated licenses will use Level 6 (extra-channels)
            </div>
            
            <form id="licenseForm">
                <div class="form-group">
                    <label>License Type</label>
                    <select name="license_type" id="licenseType" required>
                        <option value="ros">RouterOS License</option>
                        <option value="chr">CHR License</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Software/System ID</label>
                    <input type="text" name="software_id" id="softwareId" placeholder="e.g., 4JZ2-H049" required>
                </div>
                
                <button type="submit" class="generate-btn" id="generateBtn">
                    Generate License
                </button>
            </form>
            
            <div class="loading" id="loading">
                <div class="loading-spinner"></div>
                Generating license...
            </div>
            
            <div class="license-container" id="result">
                <button class="copy-btn" id="copyBtn">?? Copy</button>
                <div class="license-text" id="licenseText"></div>
            </div>
        </div>

        <script>
            // Update placeholder based on license type
            const licenseType = document.getElementById('licenseType');
            const softwareIdInput = document.getElementById('softwareId');
            
            licenseType.addEventListener('change', function() {
                if (this.value === 'ros') {
                    softwareIdInput.placeholder = 'e.g., 4JZ2-H049';
                } else {
                    softwareIdInput.placeholder = 'e.g., pjLQ21gHzfI';
                }
            });

            // Copy functionality
            function copyLicense() {
                const licenseText = document.getElementById('licenseText').textContent;
                navigator.clipboard.writeText(licenseText).then(function() {
                    const copyBtn = document.getElementById('copyBtn');
                    copyBtn.textContent = 'Copied!';
                    copyBtn.classList.add('copied');
                    
                    setTimeout(() => {
                        copyBtn.textContent = 'Copy';
                        copyBtn.classList.remove('copied');
                    }, 2000);
                }).catch(function(err) {
                    alert('Copy failed. Please select and copy manually.');
                    console.error('Copy failed: ', err);
                });
            }

            // Form submission
            document.getElementById('licenseForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const formData = new FormData(this);
                const generateBtn = document.getElementById('generateBtn');
                const loading = document.getElementById('loading');
                const result = document.getElementById('result');
                const licenseText = document.getElementById('licenseText');
                const copyBtn = document.getElementById('copyBtn');
                
                // UI states
                generateBtn.disabled = true;
                result.style.display = 'none';
                loading.style.display = 'block';
                copyBtn.textContent = 'Copy'; // Reset copy button
                
                try {
                    const response = await fetch('/generate', { 
                        method: 'POST', 
                        body: formData 
                    });
                    
                    if (!response.ok) throw new Error('Network error');
                    
                    const data = await response.json();
                    
                    // Show result
                    licenseText.textContent = data.license;
                    result.style.display = 'block';
                    loading.style.display = 'none';
                    
                    // Scroll to result smoothly
                    result.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'center' 
                    });
                    
                } catch (error) {
                    licenseText.textContent = 'Error: ' + error.message;
                    result.style.display = 'block';
                    loading.style.display = 'none';
                } finally {
                    generateBtn.disabled = false;
                }
            });

            // Event listeners
            document.getElementById('copyBtn').addEventListener('click', copyLicense);
            
            // Auto-focus on input for better mobile UX
            softwareIdInput.focus();
            
            // Prevent form resubmission on page refresh
            if (window.history.replaceState) {
                window.history.replaceState(null, null, window.location.href);
            }
        </script>
    </body>
    </html>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    software_id = request.form['software_id']
    license_type = request.form['license_type']
    
    license_key = generate_license(software_id, license_type)
    
    return jsonify({'license': license_key})

if __name__ == '__main__':
    print("Starting MikroTik License Generator...")
    print("Optimized for Mobile Devices")
    print("Fixed License Level: 6")
    print("Web Interface: http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=True)
