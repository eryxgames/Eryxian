import React, { useState, useEffect, useRef } from 'react';
import { Search, Filter, Play, Pause, SkipBack, SkipForward, Volume2, BookOpen, Home, Library, User, X, Menu, Star, Clock, Download } from 'lucide-react';

const BookReaderApp = () => {
  const [currentView, setCurrentView] = useState('home');
  const [books, setBooks] = useState([]);
  const [filteredBooks, setFilteredBooks] = useState([]);
  const [currentBook, setCurrentBook] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('title');
  const [filterGenre, setFilterGenre] = useState('all');
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [showFilters, setShowFilters] = useState(false);
  const [readingProgress, setReadingProgress] = useState({});
  const audioRef = useRef(null);

  // Sample book data
  useEffect(() => {
    const sampleBooks = [
      {
        id: 1,
        title: "The Digital Revolution",
        author: "Sarah Chen",
        genre: "Technology",
        format: "md",
        cover: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=400&fit=crop",
        description: "A comprehensive guide to understanding modern technology trends.",
        content: "# The Digital Revolution\n\n## Chapter 1: Introduction\n\nThe digital revolution has transformed our world...",
        rating: 4.5,
        pages: 280,
        publishDate: "2024"
      },
      {
        id: 2,
        title: "Mindful Living",
        author: "David Kumar",
        genre: "Self-Help",
        format: "epub",
        cover: "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=300&h=400&fit=crop",
        description: "Discover the art of mindful living in our fast-paced world.",
        content: "Chapter 1: The Path to Mindfulness\n\nMindfulness is not just a practice...",
        rating: 4.8,
        pages: 195,
        publishDate: "2023"
      },
      {
        id: 3,
        title: "Ocean Mysteries",
        author: "Dr. Marina Lopez",
        genre: "Science",
        format: "audiobook",
        cover: "https://images.unsplash.com/photo-1439066615861-d1af74d74000?w=300&h=400&fit=crop",
        description: "Explore the hidden depths of our planet's oceans.",
        audioUrl: "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
        rating: 4.3,
        duration: "8h 32m",
        publishDate: "2024"
      },
      {
        id: 4,
        title: "Quantum Physics Simplified",
        author: "Prof. James Wright",
        genre: "Science",
        format: "md",
        cover: "https://images.unsplash.com/photo-1636466497217-26a8cbeaf0aa?w=300&h=400&fit=crop",
        description: "Understanding quantum mechanics made accessible.",
        content: "# Quantum Physics Simplified\n\n## The Quantum World\n\nQuantum physics challenges our understanding...",
        rating: 4.6,
        pages: 340,
        publishDate: "2023"
      }
    ];
    setBooks(sampleBooks);
    setFilteredBooks(sampleBooks);
  }, []);

  // Filter and search functionality
  useEffect(() => {
    let filtered = books.filter(book => {
      const matchesSearch = book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           book.author.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           book.genre.toLowerCase().includes(searchTerm.toLowerCase());
      const matchesGenre = filterGenre === 'all' || book.genre === filterGenre;
      return matchesSearch && matchesGenre;
    });

    // Sort books
    filtered.sort((a, b) => {
      switch(sortBy) {
        case 'author':
          return a.author.localeCompare(b.author);
        case 'genre':
          return a.genre.localeCompare(b.genre);
        case 'rating':
          return b.rating - a.rating;
        case 'date':
          return b.publishDate.localeCompare(a.publishDate);
        default:
          return a.title.localeCompare(b.title);
      }
    });

    setFilteredBooks(filtered);
  }, [books, searchTerm, sortBy, filterGenre]);

  // Audio controls
  const togglePlayPause = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const handleTimeUpdate = () => {
    if (audioRef.current) {
      setCurrentTime(audioRef.current.currentTime);
    }
  };

  const handleLoadedMetadata = () => {
    if (audioRef.current) {
      setDuration(audioRef.current.duration);
    }
  };

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  const openBook = (book) => {
    setCurrentBook(book);
    setCurrentView('reader');
  };

  const genres = [...new Set(books.map(book => book.genre))];

  const PromoBanner = () => (
    <div className="bg-gradient-to-r from-purple-600 to-blue-600 text-white p-4 rounded-lg mb-6 relative overflow-hidden">
      <div className="relative z-10">
        <h3 className="text-lg font-bold mb-2">🎉 Premium Reading Experience</h3>
        <p className="text-sm opacity-90 mb-3">Unlock unlimited books and exclusive content</p>
        <button className="bg-white text-purple-600 px-4 py-2 rounded-full text-sm font-semibold hover:bg-gray-100 transition-colors">
          Get Premium
        </button>
      </div>
      <div className="absolute right-0 top-0 w-32 h-full bg-white/10 transform skew-x-12 translate-x-8"></div>
    </div>
  );

  const BookCard = ({ book }) => (
    <div className="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow cursor-pointer"
         onClick={() => openBook(book)}>
      <div className="flex space-x-3">
        <img src={book.cover} alt={book.title} className="w-16 h-20 object-cover rounded" />
        <div className="flex-1 min-w-0">
          <h3 className="font-semibold text-gray-900 truncate">{book.title}</h3>
          <p className="text-sm text-gray-600 truncate">{book.author}</p>
          <div className="flex items-center space-x-2 mt-1">
            <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded">{book.genre}</span>
            <span className="text-xs text-gray-500">{book.format.toUpperCase()}</span>
          </div>
          <div className="flex items-center space-x-2 mt-2">
            <div className="flex items-center">
              <Star className="w-3 h-3 fill-yellow-400 text-yellow-400" />
              <span className="text-xs text-gray-600 ml-1">{book.rating}</span>
            </div>
            {book.pages && <span className="text-xs text-gray-500">{book.pages} pages</span>}
            {book.duration && <span className="text-xs text-gray-500">{book.duration}</span>}
          </div>
        </div>
      </div>
    </div>
  );

  const renderContent = () => {
    switch(currentView) {
      case 'home':
        return (
          <div className="space-y-6">
            <PromoBanner />
            
            <div>
              <h2 className="text-xl font-bold text-gray-900 mb-4">Recently Added</h2>
              <div className="grid grid-cols-2 gap-4">
                {filteredBooks.slice(0, 4).map(book => (
                  <div key={book.id} className="bg-white rounded-lg shadow-md p-3 cursor-pointer hover:shadow-lg transition-shadow"
                       onClick={() => openBook(book)}>
                    <img src={book.cover} alt={book.title} className="w-full h-32 object-cover rounded mb-2" />
                    <h3 className="font-medium text-sm text-gray-900 truncate">{book.title}</h3>
                    <p className="text-xs text-gray-600 truncate">{book.author}</p>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <h2 className="text-xl font-bold text-gray-900 mb-4">Continue Reading</h2>
              <div className="bg-white rounded-lg shadow-md p-4">
                <div className="flex items-center space-x-3">
                  <Clock className="w-5 h-5 text-blue-600" />
                  <div>
                    <p className="font-medium text-gray-900">The Digital Revolution</p>
                    <p className="text-sm text-gray-600">Progress: 65%</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        );

      case 'library':
        return (
          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <div className="flex-1 relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                <input
                  type="text"
                  placeholder="Search books, authors, genres..."
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>
              <button
                onClick={() => setShowFilters(!showFilters)}
                className="p-2 border border-gray-300 rounded-lg hover:bg-gray-50"
              >
                <Filter className="w-4 h-4" />
              </button>
            </div>

            {showFilters && (
              <div className="bg-white p-4 rounded-lg shadow-md space-y-3">
                <div>
                  <label className="text-sm font-medium text-gray-700 mb-1 block">Sort by</label>
                  <select
                    value={sortBy}
                    onChange={(e) => setSortBy(e.target.value)}
                    className="w-full p-2 border border-gray-300 rounded"
                  >
                    <option value="title">Title</option>
                    <option value="author">Author</option>
                    <option value="genre">Genre</option>
                    <option value="rating">Rating</option>
                    <option value="date">Date</option>
                  </select>
                </div>
                <div>
                  <label className="text-sm font-medium text-gray-700 mb-1 block">Genre</label>
                  <select
                    value={filterGenre}
                    onChange={(e) => setFilterGenre(e.target.value)}
                    className="w-full p-2 border border-gray-300 rounded"
                  >
                    <option value="all">All Genres</option>
                    {genres.map(genre => (
                      <option key={genre} value={genre}>{genre}</option>
                    ))}
                  </select>
                </div>
              </div>
            )}

            <div className="space-y-3">
              {filteredBooks.map(book => (
                <BookCard key={book.id} book={book} />
              ))}
            </div>
          </div>
        );

      case 'reader':
        return currentBook && (
          <div className="bg-white rounded-lg shadow-sm">
            <div className="flex items-center justify-between p-4 border-b">
              <button
                onClick={() => setCurrentView('library')}
                className="p-2 hover:bg-gray-100 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
              <h1 className="font-semibold text-gray-900 text-center flex-1 mx-4 truncate">
                {currentBook.title}
              </h1>
              <button className="p-2 hover:bg-gray-100 rounded-lg">
                <Download className="w-5 h-5" />
              </button>
            </div>

            {currentBook.format === 'audiobook' ? (
              <div className="p-6">
                <div className="text-center mb-6">
                  <img src={currentBook.cover} alt={currentBook.title} 
                       className="w-48 h-48 object-cover rounded-lg mx-auto mb-4" />
                  <h2 className="text-xl font-bold text-gray-900">{currentBook.title}</h2>
                  <p className="text-gray-600">{currentBook.author}</p>
                </div>

                <div className="bg-gray-100 rounded-lg p-4 mb-6">
                  <div className="flex justify-between text-sm text-gray-600 mb-2">
                    <span>{formatTime(currentTime)}</span>
                    <span>{formatTime(duration)}</span>
                  </div>
                  <div className="w-full bg-gray-300 rounded-full h-2">
                    <div 
                      className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${(currentTime / duration) * 100 || 0}%` }}
                    ></div>
                  </div>
                </div>

                <div className="flex items-center justify-center space-x-6">
                  <button className="p-3 hover:bg-gray-100 rounded-full">
                    <SkipBack className="w-6 h-6" />
                  </button>
                  <button 
                    onClick={togglePlayPause}
                    className="p-4 bg-blue-600 text-white rounded-full hover:bg-blue-700"
                  >
                    {isPlaying ? <Pause className="w-8 h-8" /> : <Play className="w-8 h-8" />}
                  </button>
                  <button className="p-3 hover:bg-gray-100 rounded-full">
                    <SkipForward className="w-6 h-6" />
                  </button>
                </div>

                <audio
                  ref={audioRef}
                  src={currentBook.audioUrl}
                  onTimeUpdate={handleTimeUpdate}
                  onLoadedMetadata={handleLoadedMetadata}
                  onEnded={() => setIsPlaying(false)}
                />
              </div>
            ) : (
              <div className="p-6 max-w-none prose prose-slate">
                {currentBook.format === 'md' ? (
                  <div dangerouslySetInnerHTML={{ 
                    __html: currentBook.content.replace(/\n/g, '<br />').replace(/# /g, '<h1>').replace(/<br \/><br \/>/g, '</h1><br />').replace(/## /g, '<h2>').replace(/<br \/>/g, '</h2><p>') + '</p>'
                  }} />
                ) : (
                  <div className="whitespace-pre-wrap leading-relaxed text-gray-800">
                    {currentBook.content}
                  </div>
                )}
              </div>
            )}
          </div>
        );

      default:
        return <div>Page not found</div>;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b sticky top-0 z-10">
        <div className="max-w-md mx-auto px-4 py-3">
          <div className="flex items-center justify-between">
            <h1 className="text-xl font-bold text-gray-900">BookReader</h1>
            <div className="flex items-center space-x-2">
              <button className="p-2 hover:bg-gray-100 rounded-lg">
                <Search className="w-5 h-5 text-gray-600" />
              </button>
              <button className="p-2 hover:bg-gray-100 rounded-lg">
                <Menu className="w-5 h-5 text-gray-600" />
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-md mx-auto px-4 py-6 pb-20">
        {renderContent()}
      </main>

      {/* Bottom Navigation */}
      <nav className="fixed bottom-0 left-0 right-0 bg-white border-t shadow-lg">
        <div className="max-w-md mx-auto">
          <div className="flex items-center justify-around py-2">
            <button
              onClick={() => setCurrentView('home')}
              className={`flex flex-col items-center py-2 px-3 rounded-lg ${
                currentView === 'home' ? 'text-blue-600 bg-blue-50' : 'text-gray-600'
              }`}
            >
              <Home className="w-5 h-5" />
              <span className="text-xs mt-1">Home</span>
            </button>
            <button
              onClick={() => setCurrentView('library')}
              className={`flex flex-col items-center py-2 px-3 rounded-lg ${
                currentView === 'library' ? 'text-blue-600 bg-blue-50' : 'text-gray-600'
              }`}
            >
              <Library className="w-5 h-5" />
              <span className="text-xs mt-1">Library</span>
            </button>
            <button
              onClick={() => setCurrentView('reader')}
              className={`flex flex-col items-center py-2 px-3 rounded-lg ${
                currentView === 'reader' ? 'text-blue-600 bg-blue-50' : 'text-gray-600'
              }`}
            >
              <BookOpen className="w-5 h-5" />
              <span className="text-xs mt-1">Reading</span>
            </button>
            <button
              className="flex flex-col items-center py-2 px-3 rounded-lg text-gray-600"
            >
              <User className="w-5 h-5" />
              <span className="text-xs mt-1">Profile</span>
            </button>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default BookReaderApp;