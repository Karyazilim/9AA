# 9-Anadolu A Student Directory

A Flask-based student directory web application for the class "9-Anadolu A" with search functionality and a modern UI design.

## Features

- **Student List**: Alphabetically organized student directory with letter groupings (A-Z)
- **Search Functionality**: Real-time search to filter students by name
- **Responsive Design**: Mobile-first design with Tailwind-inspired styling
- **Navigation Footer**: Navigation tabs with Students tab active
- **Student Detail Pages**: Individual pages for each student

## Tech Stack

- **Backend**: Python 3.x + Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS (Tailwind-inspired without external dependencies)
- **Icons**: Text-based icons (emojis and symbols)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Karyazilim/9AA.git
cd 9AA
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
9AA/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main template
└── README.md          # This file
```

## Routes

- `GET /` - Main student directory page
- `GET /students/<name>` - Individual student detail page
- `GET /api/search?q=<query>` - Search API endpoint

## Student Data

The application includes sample data for 28 students with names from A-Z. Each student is assigned a colored avatar based on their first letter.

## Features Implemented

✅ Flask application structure
✅ Student list with alphabetical grouping
✅ Real-time search functionality
✅ Mobile-responsive design
✅ Footer navigation with active state
✅ Student detail pages
✅ Color-coded avatars by letter
✅ No results message for search
✅ Sticky header and search bar

## Design

The application follows the provided design specifications with:
- Clean, modern interface
- Sticky header with class name "9-Anadolu A"
- Search bar with search icon
- Alphabetical letter headers
- Student items with avatars and names
- Navigation footer with appropriate icons
- Consistent color scheme and typography

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers
- No external dependencies required