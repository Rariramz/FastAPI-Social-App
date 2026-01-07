from fastapi import HTTPException, APIRouter
from app.schemas import PostCreate, PostRead


router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

text_posts = {
    1: { "title": "Post 1", "content": "Post 1 content" },
    2: { "title": "Post 2", "content": "Post 2 content" },
    3: { "title": "Post 3", "content": "Post 3 content" },
    4: { "title": "Post 4", "content": "Post 4 content" },
    5: { "title": "Post 5", "content": "Post 5 content" },
    6: { "title": "Post 6", "content": "Post 6 content" },
    7: { "title": "Post 7", "content": "Post 7 content" },
    8: { "title": "Post 8", "content": "Post 8 content" },
    9: { "title": "Post 9", "content": "Post 9 content" },
    10: { "title": "Post 10", "content": "Post 10 content" },
}

@router.get('/', response_model=list[PostRead])
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@router.get('/{post_id}', response_model=PostRead)
def get_all_posts(post_id: int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(post_id)

@router.post('/', response_model=PostRead)
def create_post(post: PostCreate):
    new_post = { 'title': post.title, 'content': post.content }
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

@router.delete('/{post_id}', response_model=PostRead)
def delete_post(post_id: int):
    deleted_post = text_posts.pop(post_id, None)
    return deleted_post