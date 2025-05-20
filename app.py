from flask import Flask, request, render_template_string

app = Flask(__name__)

phones = {
    "iPhone 15 Pro Max": {
        "Build": {
            "Body": "Titanium frame, Ceramic Shield front",
            "Dimensions": "159.9 x 76.7 x 8.25 mm",
            "Weight": "221g",
            "Protection": "IP68 dust/water resistant",
            "Materials": "Aerospace-grade titanium, back glass",
            "Resistance": "Water resistant up to 6m for 30 min",
            "Other": "Ceramic Shield is tougher than any smartphone glass"
        },
        "Technical Details": {
            "Chipset": "A17 Pro (3 nm)",
            "RAM": "8GB",
            "Storage": "128GB / 256GB / 512GB / 1TB",
            "Battery": "4422mAh",
            "Display": "6.7\" Super Retina XDR OLED, 120Hz",
            "Camera": "Triple 48MP + 12MP + 12MP",
            "GPU": "Apple GPU (6-core graphics)",
            "Video": "ProRes, Cinematic mode (4K at 30 fps)",
            "OS": "iOS 17 (upgradable)",
            "Sensors": "Face ID, Accelerometer, Gyro, Barometer, Compass"
        },
        "Pricing & Sellers": {
            "Amazon": "₹1,39,900",
            "Flipkart": "₹1,37,999",
            "Apple Store": "₹1,39,900",
            "Bank Offer": "₹5,000 Instant Discount on HDFC Cards",
            "EMI": "Starting ₹4,599/month"
        }
    },
    "Samsung Galaxy S23 Ultra": {
        "Build": {
            "Body": "Aluminum frame, Gorilla Glass Victus 2",
            "Dimensions": "163.4 x 78.1 x 8.9 mm",
            "Weight": "234g",
            "Protection": "IP68 dust/water resistant"
        },
        "Technical Details": {
            "Chipset": "Snapdragon 8 Gen 2",
            "RAM": "8GB / 12GB",
            "Storage": "256GB / 512GB / 1TB",
            "Battery": "5000mAh",
            "Display": "6.8\" Dynamic AMOLED 2X, 120Hz",
            "Camera": "Quad 200MP + 10MP + 10MP + 12MP",
            "OS": "Android 13, One UI 5.1"
        },
        "Pricing & Sellers": {
            "Amazon": "₹1,09,999",
            "Flipkart": "₹1,07,999"
        }
    },
    # Additional 18 phones (brief specs for demo)
    "Google Pixel 8 Pro": {
        "Build": {"Body": "Aluminum frame, Gorilla Glass Victus"},
        "Technical Details": {"Chipset": "Google Tensor G3", "RAM": "12GB", "Battery": "5000mAh"},
        "Pricing & Sellers": {"Amazon": "₹89,999"}
    },
    "OnePlus 11": {
        "Build": {"Body": "Aluminum frame, Gorilla Glass"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "16GB", "Battery": "5000mAh"},
        "Pricing & Sellers": {"Amazon": "₹56,999"}
    },
    "Xiaomi 13 Pro": {
        "Build": {"Body": "Glass front/back, aluminum frame"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "12GB", "Battery": "4820mAh"},
        "Pricing & Sellers": {"Flipkart": "₹71,999"}
    },
    "Samsung Galaxy Z Fold 5": {
        "Build": {"Body": "Aluminum frame, foldable"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "12GB", "Battery": "4400mAh"},
        "Pricing & Sellers": {"Samsung Store": "₹1,84,999"}
    },
    "iPhone 14 Pro Max": {
        "Build": {"Body": "Stainless steel, Ceramic Shield"},
        "Technical Details": {"Chipset": "A16 Bionic", "RAM": "6GB", "Battery": "4323mAh"},
        "Pricing & Sellers": {"Apple Store": "₹1,29,900"}
    },
    "Sony Xperia 1 IV": {
        "Build": {"Body": "Aluminum frame, Gorilla Glass"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 1", "RAM": "12GB", "Battery": "5000mAh"},
        "Pricing & Sellers": {"Amazon": "₹84,990"}
    },
    "Motorola Edge 40 Pro": {
        "Build": {"Body": "Aluminum frame, glass back"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "12GB", "Battery": "4600mAh"},
        "Pricing & Sellers": {"Flipkart": "₹54,999"}
    },
    "Asus ROG Phone 7": {
        "Build": {"Body": "Glass front/back, aluminum frame"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "16GB", "Battery": "6000mAh"},
        "Pricing & Sellers": {"Amazon": "₹79,999"}
    },
    "Realme GT 3": {
        "Build": {"Body": "Glass front/back"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "12GB", "Battery": "4500mAh"},
        "Pricing & Sellers": {"Flipkart": "₹38,999"}
    },
    "Vivo X90 Pro+": {
        "Build": {"Body": "Glass front/back"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "12GB", "Battery": "4870mAh"},
        "Pricing & Sellers": {"Amazon": "₹69,999"}
    },
    "Oppo Find X6 Pro": {
        "Build": {"Body": "Glass front/back, aluminum frame"},
        "Technical Details": {"Chipset": "Snapdragon 8 Gen 2", "RAM": "12GB", "Battery": "5000mAh"},
        "Pricing & Sellers": {"Flipkart": "₹69,999"}
    },
    "Samsung Galaxy A54": {
        "Build": {"Body": "Plastic frame, glass front"},
        "Technical Details": {"Chipset": "Exynos 1380", "RAM": "6GB", "Battery": "5000mAh"},
        "Pricing & Sellers": {"Amazon": "₹26,999"}
    },
    "iPhone SE 2022": {
        "Build": {"Body": "Glass front/back, aluminum frame"},
        "Technical Details": {"Chipset": "A15 Bionic", "RAM": "4GB", "Battery": "2018mAh"},
        "Pricing & Sellers": {"Apple Store": "₹43,900"}
    },
    "Samsung Galaxy S22": {
        "Build": {"Body": "Aluminum frame, Gorilla Glass Victus"},
        "Technical Details": {"Chipset": "Exynos 2200", "RAM": "8GB", "Battery": "3700mAh"},
        "Pricing & Sellers": {"Flipkart": "₹65,999"}
    },
    "Google Pixel 7": {
        "Build": {"Body": "Aluminum frame, Gorilla Glass Victus"},
        "Technical Details": {"Chipset": "Google Tensor G2", "RAM": "8GB", "Battery": "4355mAh"},
        "Pricing & Sellers": {"Amazon": "₹49,999"}
    },
    "OnePlus Nord 3": {
        "Build": {"Body": "Glass front/back"},
        "Technical Details": {"Chipset": "MediaTek Dimensity 9200+", "RAM": "8GB", "Battery": "4500mAh"},
        "Pricing & Sellers": {"Amazon": "₹31,999"}
    },
    "Xiaomi Redmi Note 12 Pro+": {
        "Build": {"Body": "Glass front/back"},
        "Technical Details": {"Chipset": "MediaTek Dimensity 1080", "RAM": "8GB", "Battery": "4500mAh"},
        "Pricing & Sellers": {"Flipkart": "₹18,999"}
    },
    "Realme Narzo 60 5G": {
        "Build": {"Body": "Plastic frame"},
        "Technical Details": {"Chipset": "MediaTek Helio G85", "RAM": "4GB", "Battery": "5000mAh"},
        "Pricing & Sellers": {"Amazon": "₹10,499"}
    },
}

@app.route('/', methods=['GET', 'POST'])
def compare_phones():
    result = ""
    if request.method == 'POST':
        phone1 = request.form.get('phone1')
        phone2 = request.form.get('phone2')
        p1 = phones.get(phone1)
        p2 = phones.get(phone2)

        if not p1 or not p2:
            result = "<div class='alert alert-danger'>Please select two valid phones.</div>"
        else:
            # Collect all categories and keys to create a full comparison
            categories = set(p1.keys()) | set(p2.keys())
            comparison = {}
            for cat in categories:
                keys = set()
                if cat in p1:
                    keys |= p1[cat].keys()
                if cat in p2:
                    keys |= p2[cat].keys()
                comparison[cat] = []
                for key in keys:
                    val1 = p1.get(cat, {}).get(key, "N/A")
                    val2 = p2.get(cat, {}).get(key, "N/A")
                    comparison[cat].append((key, val1, val2))

            # Render comparison table
            result = render_template_string("""
            <h2 class="mt-4">Comparison: {{phone1}} vs {{phone2}}</h2>
            {% for category, items in comparison.items() %}
                <h4 class="mt-3">{{ category }}</h4>
                <table class="table table-bordered table-striped">
                    <thead class="table-dark">
                        <tr>
                            <th>Specification</th>
                            <th>{{ phone1 }}</th>
                            <th>{{ phone2 }}</th>
                        </tr>
                    </thead>
                    <tbody>
                    {% for spec, val1, val2 in items %}
                        <tr>
                            <td>{{ spec }}</td>
                            <td>{{ val1 }}</td>
                            <td>{{ val2 }}</td>
                        </tr>
                    {% endfor %}
                    </tbody>
                </table>
            {% endfor %}
            <a href="/" class="btn btn-primary mt-3">Compare Another</a>
            """, phone1=phone1, phone2=phone2, comparison=comparison)

    # Form page
    phone_names = sorted(phones.keys())
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Phone Comparison</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS CDN -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
                padding-top: 50px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .container {
                max-width: 900px;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 25px rgba(0,0,0,0.1);
            }
            h1 {
                font-weight: 700;
                color: #333;
            }
            label {
                font-weight: 600;
            }
            select.form-select {
                cursor: pointer;
            }
            button {
                font-weight: 600;
            }
            table th, table td {
                vertical-align: middle !important;
            }
        </style>
    </head>
    <body>
        <div class="container shadow-sm">
            <h1 class="mb-4 text-center">Compare Smartphones</h1>
            <form method="POST">
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="phone1" class="form-label">Select First Phone</label>
                        <select class="form-select" id="phone1" name="phone1" required>
                            <option value="" disabled selected>Choose a phone</option>
                            {% for phone in phone_names %}
                                <option value="{{ phone }}">{{ phone }}</option>
                            {% endfor %}
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="phone2" class="form-label">Select Second Phone</label>
                        <select class="form-select" id="phone2" name="phone2" required>
                            <option value="" disabled selected>Choose a phone</option>
                            {% for phone in phone_names %}
                                <option value="{{ phone }}">{{ phone }}</option>
                            {% endfor %}
                        </select>
                    </div>
                </div>
                <div class="d-grid gap-2 col-6 mx-auto">
                    <button type="submit" class="btn btn-primary btn-lg">Compare</button>
                </div>
            </form>
            <div>
                {{ result|safe }}
            </div>
        </div>
    </body>
    </html>
    """, phone_names=phone_names, result=result)

if __name__ == '__main__':
    app.run(debug=True)
