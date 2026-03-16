from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Video, VideoCategory
from .forms import VideoForm

# 首页：展示所有视频
def index(request):
    videos = Video.objects.all().order_by("-created_at")
    categories = VideoCategory.objects.all()
    return render(request, "video/index.html", {
        "videos": videos,
        "categories": categories
    })

# 视频详情页
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.view_count += 1  # 播放量+1
    video.save()
    return render(request, "video/detail.html", {"video": video})

# 分类页：展示某分类下的所有视频
def category_videos(request, slug):
    category = get_object_or_404(VideoCategory, slug=slug)
    videos = Video.objects.filter(category=category).order_by("-created_at")
    return render(request, "video/category.html", {
        "category": category,
        "videos": videos
    })

# 上传视频（需要登录）
@login_required
def upload_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploader = request.user
            video.save()
            return redirect("video_detail", pk=video.pk)
    else:
        form = VideoForm()
    return render(request, "video/upload.html", {"form": form})