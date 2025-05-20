<?php
session_start();
$db = new SQLite3('db/user_db.sqlite');

$email = $_POST['email'];
$password = $_POST['password'];

$stmt = $db->prepare("SELECT * FROM users WHERE email = :email");
$stmt->bindValue(':email', $email);
$result = $stmt->execute();

$user = $result->fetchArray(SQLITE3_ASSOC);

if ($user && password_verify($password, $user['password'])) {
    $_SESSION['user_id'] = $user['id'];
    $_SESSION['username'] = $user['username'];
    header('Location: index.html');
    exit();
} else {
    echo "<script>alert('Invalid login credentials.'); window.location.href='index.html';</script>";
    exit();
}
?>
