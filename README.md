# Artistic Array 🎨

**Artistic Array** is a web application built with **Django** and **Bootstrap**, designed to showcase and manage a wide collection of artworks. It supports user authentication, interactive reviews, favoriting, and advanced filtering — offering a clean and intuitive user experience without relying on frontend frameworks like React or Angular.

## ✨ Features

- 🎭 **Art Categories**  
  Explore artworks grouped into various art types and styles.

- 🔐 **User Authentication**  
  Secure login and registration system using Django’s built-in auth.

- ⭐ **Reviews & Ratings**  
  Authenticated users can submit reviews and rate individual artworks.

- ❤️ **Favorites List**  
  Logged-in users can add artworks to a personal favorites list.

- ❌ **Remove Favorites**  
  Users can remove items from their favorites with a single click.

- 🎨 **Advanced Filtering**  
  Filter artworks by:
  - Color
  - Art type
  - Popularity (rating)
  - Created time

- 📚 **Pagination**  
  Efficient navigation through large art collections with paginated views.

## 🛠 Tech Stack

- **Backend:** Python 3, Django  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Database:** SQLite (default) or PostgreSQL (optional)  
- **Authentication:** Django built-in user model with login/registration

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/artistic-array.git
cd artistic-array

# Set up a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

# Home Page
![2023-09-23 - 20-45-10 - Artistic Array - An Online Platform to Share Your Arts](https://github.com/hridoyroybu/artistic-array/assets/37092647/9f57f509-66e0-467a-b904-0e2343422bea)

# All Arts
![2023-09-23 - 21-16-00 - Artistic Array - An Online Platform to Share Your Arts](https://github.com/hridoyroybu/artistic-array/assets/37092647/ca5e9a6d-95b0-4bb1-849d-6b86ae319f5c)

# Art Details
![2023-09-23 - 20-45-53 - Artistic Array - An Online Platform to Share Your Arts](https://github.com/hridoyroybu/artistic-array/assets/37092647/b1b29a36-7638-4716-b08c-f246d0cd517f)

# Favourite Arts
![2023-09-23 - 20-46-08 - Artistic Array - An Online Platform to Share Your Arts](https://github.com/hridoyroybu/artistic-array/assets/37092647/9e39444c-913b-4e29-b7d6-584a02770e12)
