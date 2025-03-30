# utils/html_generator.py
from utils.themes import get_theme_colors


def generate_html_contract(contract, theme_name):
    """Generate HTML representation of the contract"""

    # Get theme colors
    theme = get_theme_colors(theme_name)

    # Basic HTML template with CSS
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{contract.title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Georgia:wght@300;400;500;700&display=swap');
        
        :root {{
            --primary-color: {theme["primary_color"]};
            --secondary-color: {theme["secondary_color"]};
            --accent-color: {theme["accent_color"]};
            --text-color: {theme["text_color"]};
            --light-color: {theme["light_color"]};
            --border-color: {theme["border_color"]};
            --light-purple: {theme["highlight_color"]};
            --deep-red: {theme["deep_color"]};
        }}
        
        body {{
            font-family: {theme["font_family"]};
            line-height: 1.6;
            color: var(--text-color);
            background-color: white;
            margin: 0;
            padding: 0;
        }}
        
        .container {{
            max-width: 850px;
            margin: 0 auto;
            padding: 0;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            position: relative;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200"><path d="M20,100 C20,60 60,20 100,20 C140,20 180,60 180,100 C180,140 140,180 100,180 C60,180 20,140 20,100 Z" stroke="rgba(76, 201, 240, 0.03)" fill="none" stroke-width="10"/></svg>');
            background-size: 400px;
            background-position: center;
            background-repeat: repeat;
        }}
        
        .banner-container {{
            position: relative;
            height: 150px;
            background: {theme["banner_gradient"]};
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            margin-bottom: -5px;
        }}

        .banner-text {{
            color: white;
            text-align: center;
            z-index: 2;
        }}

        .banner-title {{
            font-family: 'Arial Black', sans-serif;
            font-size: 3rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            margin: 0;
        }}

        .banner-tagline {{
            font-style: italic;
            font-size: 1.2rem;
            margin-top: 0.5rem;
        }}
        
        .header {{
            background: {theme["header_gradient"]};
            color: white;
            padding: 20px 40px;
            border-bottom: 5px solid var(--accent-color);
            position: relative;
            overflow: hidden;
        }}
        
        .header::after {{
            content: "";
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><path d="M50 0 L100 50 L50 100 L0 50 Z" fill="rgba(255,255,255,0.05)"/></svg>');
            background-size: 80px 80px;
            opacity: 0.3;
        }}
        
        .header h1 {{
            margin: 0 0 10px 0;
            font-size: 2.5rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }}
        
        .header p {{
            margin: 0;
            font-size: 1.2rem;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 30px 40px;
        }}
        
        .effective-date {{
            font-style: italic;
            color: #666;
            margin-bottom: 15px;
        }}
        
        .highlight {{
            color: var(--secondary-color);
            font-weight: 600;
            background-color: rgba(247, 37, 133, 0.08);
            padding: 0 4px;
            border-radius: 3px;
        }}
        
        .divider {{
            height: 1px;
            background: linear-gradient(to right, transparent, var(--border-color), transparent);
            margin: 20px 0;
        }}
        
        .parties {{
            display: flex;
            justify-content: space-between;
            padding: 30px 40px;
            background-color: #f8f9fa;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .party {{
            flex: 1;
            padding: 0 20px;
            position: relative;
        }}
        
        .party:first-child {{
            border-right: 1px solid var(--border-color);
            padding-left: 0;
        }}
        
        .party:last-child {{
            padding-right: 0;
        }}
        
        .party h3 {{
            color: var(--primary-color);
            margin-top: 0;
            font-size: 1.3rem;
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 8px;
            display: inline-block;
        }}
        
        .party h3::before {{
            content: "";
            display: inline-block;
            width: 18px;
            height: 18px;
            margin-right: 8px;
            vertical-align: middle;
        }}
        
        .party:first-child h3::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .party:last-child h3::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .location-date {{
            background-color: var(--light-color);
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            border-top: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 20px;
        }}
        
        .location-date div::before {{
            content: "";
            display: inline-block;
            width: 16px;
            height: 16px;
            margin-right: 8px;
            vertical-align: middle;
        }}
        
        .location-date div:first-child::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" fill="%23f72585"/></svg>');
            background-size: cover;
        }}
        
        .location-date div:last-child::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" fill="%23f72585"/></svg>');
            background-size: cover;
        }}
        
        .section {{
            margin-bottom: 30px;
            position: relative;
            background-color: white;
            border-radius: 6px;
            padding: 15px 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        }}
        
        .section h2 {{
            color: var(--primary-color);
            margin-top: 0;
            font-size: 1.4rem;
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 8px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }}
        
        .section h2::before {{
            content: "";
            display: inline-block;
            width: 24px;
            height: 24px;
            margin-right: 10px;
        }}
        
        .section:nth-of-type(1) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section:nth-of-type(2) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.5 5.5c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zM9.8 8.9L7 23h2.1l1.8-8 2.1 2v6h2v-7.5l-2.1-2 .6-3C14.8 12 16.8 13 19 13v-2c-1.9 0-3.5-1-4.3-2.4l-1-1.6c-.4-.6-1-1-1.7-1-.3 0-.5.1-.8.1L6 8.3V13h2V9.6l1.8-.7" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section:nth-of-type(3) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2zm-7 5h5v5h-5v-5z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section:nth-of-type(4) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section:nth-of-type(5) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section:nth-of-type(6) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section:nth-of-type(7) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section:nth-of-type(8) h2::before {{
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z" fill="%233a0ca3"/></svg>');
            background-size: cover;
        }}
        
        .section ul {{
            padding-left: 20px;
            line-height: 1.8;
        }}
        
        .section ul li {{
            margin-bottom: 10px;
        }}
        
        .section p {{
            margin-bottom: 10px;
        }}
        
        .signatures {{
            padding: 30px 40px;
            display: flex;
            justify-content: space-between;
            background-color: var(--light-color);
            border-top: 1px solid var(--border-color);
        }}
        
        .signature {{
            flex: 1;
            padding: 0 15px;
        }}
        
        .signature:first-child {{
            border-right: 1px solid var(--border-color);
            padding-left: 0;
        }}
        
        .signature:last-child {{
            padding-right: 0;
        }}
        
        .signature h3 {{
            color: var(--primary-color);
            margin-top: 0;
            font-size: 1.2rem;
            margin-bottom: 20px;
        }}
        
        .signature-line {{
            border-bottom: 1px solid var(--text-color);
            padding-bottom: 5px;
            margin-bottom: 10px;
        }}
        
        .signature p {{
            margin: 5px 0;
            font-size: 0.9rem;
            color: #555;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            font-size: 0.9rem;
            color: #666;
            background-color: #f2f2f2;
            border-top: 5px solid var(--accent-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .footer p {{
            margin: 0;
        }}
        
        .qr-code {{
            width: 80px;
            height: 80px;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="10" width="20" height="20" fill="black" /><rect x="30" y="10" width="10" height="10" fill="black" /><rect x="50" y="10" width="10" height="10" fill="black" /><rect x="70" y="10" width="20" height="20" fill="black" /><rect x="10" y="30" width="10" height="10" fill="black" /><rect x="30" y="30" width="10" height="10" fill="black" /><rect x="50" y="30" width="10" height="10" fill="black" /><rect x="70" y="30" width="10" height="10" fill="black" /><rect x="10" y="50" width="10" height="10" fill="black" /><rect x="30" y="50" width="10" height="10" fill="black" /><rect x="50" y="50" width="10" height="10" fill="black" /><rect x="70" y="50" width="10" height="10" fill="black" /><rect x="10" y="70" width="20" height="20" fill="black" /><rect x="40" y="60" width="30" height="10" fill="black" /><rect x="40" y="80" width="10" height="10" fill="black" /><rect x="60" y="80" width="10" height="10" fill="black" /><rect x="80" y="60" width="10" height="30" fill="black" /></svg>');
            background-size: cover;
            margin-left: 10px;
        }}
        
        .draft-watermark {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 8rem;
            color: rgba(247, 37, 133, 0.05);
            font-weight: bold;
            pointer-events: none;
            z-index: 1;
            text-transform: uppercase;
        }}
        
        @media print {{
            body {{
                print-color-adjust: exact;
                -webkit-print-color-adjust: exact;
            }}
            
            .container {{
                box-shadow: none;
            }}
            
            .section {{
                break-inside: avoid;
            }}
            
            .signatures {{
                break-before: page;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="draft-watermark">Agreement</div>
        
        <div class="banner-container">
            <div class="banner-text">
                <h2 class="banner-title">CIRQUE AFLAME</h2>
                <p class="banner-tagline">Ignite Your Imagination!</p>
            </div>
        </div>
        
        <div class="header">
            <h1>{contract.title}</h1>
            <p>{contract.subtitle}</p>
        </div>
        
        <div class="content">
            <p class="effective-date">This Agreement (the "Agreement") is entered into as of <span class="highlight">{contract.effective_date}</span> (effective date), between <span class="highlight">{contract.client.name}</span> ("Client") and <span class="highlight">{contract.producer.company}</span>, represented by <span class="highlight">{contract.producer.name}</span> ("Producer"), with regard to the facts set forth herein. The performance will be carried out by {contract.producer.company} team member <span class="highlight">{contract.performer_name}</span> (the "Performer").</p>
            
            <div class="divider"></div>
        </div>
        
        <div class="parties">
            <div class="party">
                <h3>CLIENT</h3>
                <p><strong>Name:</strong> {contract.client.name}</p>
                <p><strong>Phone:</strong> {contract.client.phone}</p>
                <p><strong>Email:</strong> {contract.client.email}</p>
                <p><strong>Title:</strong> {contract.client.title}</p>
            </div>
            
            <div class="party">
                <h3>PRODUCER</h3>
                <p><strong>Name:</strong> {contract.producer.name}, {contract.producer.company}</p>
                <p><strong>Phone:</strong> {contract.producer.phone}</p>
                <p><strong>Email:</strong> {contract.producer.email}</p>
            </div>
        </div>
        
        <div class="location-date">
            <div>
                <strong>Location:</strong> {contract.event.location}
            </div>
            <div>
                <strong>Date:</strong> {contract.event.date}
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>1. FEES PAYABLE TO THE PERFORMER</h2>
                <ul>
                    <li>Total fee for the performance is <span class="highlight">${contract.fees.total_fee:.2f} USD</span>.</li>
                    {"<li>A <span class='highlight'>non-refundable deposit of ${contract.fees.deposit_amount:.2f} USD</span> is required within 48 hours of signing.</li>" if contract.fees.requires_deposit else ""}
                    {"<li>Remaining <span class='highlight'>balance of ${contract.fees.balance:.2f} USD</span> is due immediately upon completion of the performance.</li>" if contract.fees.requires_deposit else ""}
                    <li>Payment may also be made in advance.</li>
                    <li>'Completion' is defined as the end of the {contract.services.duration_minutes}-minute {contract.services.performance_type} or the moment the Performer ceases performing due to unforeseen circumstances. Full payment remains due unless otherwise agreed in writing.</li>
                    <li><strong>Accepted Payment Methods:</strong> {contract.fees.payment_methods}</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>2. SERVICES</h2>
                <ul>
                    <li><strong>Performance Details:</strong> One {contract.services.performance_type} (<span class="highlight">{contract.performer_name}</span>) for a {contract.services.duration_minutes}-minute staged appearance.</li>
                    <li><strong>Time:</strong> {contract.event.date} — <span class="highlight">{contract.services.performance_time}</span>, to be confirmed by mutual agreement. Verbal or written confirmation (including email or text) is sufficient and does <strong>not</strong> require a new contract.</li>
                    <li><strong>Costume:</strong> {contract.services.costume}.</li>
                    <li><strong>Music:</strong> Provided by the {contract.services.music_provided_by}.</li>
                    {f"<li><strong>Additional Services:</strong> {contract.services.additional_services}</li>" if contract.services.additional_services else ""}
                </ul>
            </div>
            
            <div class="section">
                <h2>3. CANCELLATION AND REFUND</h2>
                <ul>
                    {format_text_as_html_list(contract.cancellation.client_policy)}
                    {format_text_as_html_list(contract.cancellation.producer_policy)}
                </ul>
            </div>
            
            <div class="section">
                <h2>4. LATE ARRIVAL & CHANGE OF SCHEDULE</h2>
                <ul>
                    {format_text_as_html_list(contract.schedule.late_policy)}
                </ul>
            </div>
            
            <div class="section">
                <h2>5. OBLIGATIONS</h2>
                <p><strong>Producer:</strong></p>
                <ul>
                    {format_text_as_html_list(contract.obligations.producer_obligations)}
                </ul>
                
                <p><strong>Client:</strong></p>
                <ul>
                    {format_text_as_html_list(contract.obligations.client_obligations)}
                </ul>
                
                <p><strong>Venue Requirements:</strong></p>
                <ul>
                    {format_text_as_html_list(contract.obligations.venue_requirements)}
                </ul>
            </div>
            
            <div class="section">
                <h2>6. HEALTH AND SAFETY</h2>
                <ul>
                    {format_text_as_html_list(contract.safety.general_safety_policy)}
                </ul>
                
                <p><strong>Specific Safety Requirements:</strong></p>
                <ul>
                    {format_text_as_html_list(contract.safety.specific_requirements)}
                </ul>
            </div>
        </div>
        
        <div class="signatures">
            <div class="signature">
                <h3>CLIENT SIGNATURE</h3>
                <div class="signature-line"></div>
                <p>Name: {contract.client.name}</p>
                <p>Date: __________________</p>
            </div>
            
            <div class="signature">
                <h3>PRODUCER SIGNATURE</h3>
                <div class="signature-line"></div>
                <p>Name: {contract.producer.name}</p>
                <p>Date: __________________</p>
            </div>
        </div>
        
        <div class="footer">
            <p>© {get_current_year()} {contract.producer.company} | This document is legally binding once signed by both parties.</p>
            <div class="qr-code"></div>
        </div>
    </div>
</body>
</html>
"""

    return html


def format_text_as_html_list(text):
    """Convert text with bullet points or newlines to HTML list items"""
    if not text:
        return ""

    # Split the text by newlines
    lines = text.strip().split("\n")
    result = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # If line starts with bullet point (•), strip it
        if line.startswith("•"):
            line = line[1:].strip()

        result.append(f"<li>{line}</li>")

    return "\n".join(result)


def get_current_year():
    """Get current year for copyright"""
    import datetime

    return datetime.datetime.now().year
