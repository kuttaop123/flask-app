<?php
// db connection
$db = new SQLite3('db/user_db.sqlite');

// Create users table if not exists
$db->exec("CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)");

// Get POST data
$username = $_POST['username'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT);

// Check if user already exists
$check = $db->prepare("SELECT * FROM users WHERE email = :email");
$check->bindValue(':email', $email);
$result = $check->execute();

if ($result->fetchArray()) {
    echo "<script>alert('Email already registered.'); window.location.href='index.html';</script>";
    exit();
}

// Insert new user
$stmt = $db->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
$stmt->bindValue(':username', $username);
$stmt->bindValue(':email', $email);
$stmt->bindValue(':password', $password);
$stmt->execute();

echo "<script>alert('Registration successful! Please log in.'); window.location.href='index.html';</script>";
?>
